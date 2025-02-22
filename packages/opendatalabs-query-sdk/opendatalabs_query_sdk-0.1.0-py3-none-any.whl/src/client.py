"""
Query API SDK
A Python SDK for interacting with the Query API service.
"""

from typing import List, Dict, Optional, Any, TypedDict
import requests
import time
from dataclasses import dataclass
from urllib.parse import urlencode

class QueryAPIError(Exception):
    """Custom error class for Query API related errors"""
    def __init__(self, message: str, status_code: Optional[int] = None, response: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

# Type definitions
QueryStatusType = str  # 'queued' | 'processing' | 'completed' | 'failed'

class SchemaColumn(TypedDict):
    name: str
    type: str
    description: str

class Schema(TypedDict):
    name: str
    columns: List[SchemaColumn]

class QueryRequest(TypedDict, total=False):
    query: str  # Required
    transform: Optional[str]  # Optional
    webhook_url: Optional[str]  # Optional

class QueryStatusResponse(TypedDict):
    query_id: str
    status: QueryStatusType
    error: Optional[str]
    created_at: str

class QueryResults(TypedDict):
    results: List[Any]
    next_cursor: Optional[str]

@dataclass
class QueryClientConfig:
    """SDK configuration options"""
    api_key: str
    base_url: str
    timeout: int = 10000  # milliseconds

class QueryClient:
    """Query API SDK client"""
    
    def __init__(self, config: QueryClientConfig):
        """Creates a new Query API client instance"""
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'x-api-key': config.api_key
        })

    def _handle_response(self, response: requests.Response) -> Any:
        """Handle API response and errors"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_message = "API request failed"
            error_response = None
            
            if response.content:
                try:
                    error_response = response.json()
                    if isinstance(error_response, dict) and 'error' in error_response:
                        error_message = error_response['error']
                except ValueError:
                    pass
                    
            raise QueryAPIError(
                message=error_message,
                status_code=response.status_code if response else None,
                response=error_response
            ) from e

    def get_schemas(self) -> List[Schema]:
        """
        Get available database schemas
        
        Returns:
            List of schema definitions
        Raises:
            QueryAPIError: If the API request fails
        """
        response = self.session.get(
            f"{self.config.base_url}/v1/schemas",
            timeout=self.config.timeout / 1000  # Convert to seconds
        )
        data = self._handle_response(response)
        return data['schemas']

    def submit_query(self, request: QueryRequest) -> str:
        """
        Submit a new query for processing
        
        Args:
            request: Query request parameters
        Returns:
            Query ID string
        Raises:
            QueryAPIError: If the API request fails
        """
        response = self.session.post(
            f"{self.config.base_url}/v1/queries",
            json=request,
            timeout=self.config.timeout / 1000
        )
        data = self._handle_response(response)
        return data['query_id']

    def get_query_status(self, query_id: str) -> QueryStatusResponse:
        """
        Get status of a specific query
        
        Args:
            query_id: ID of the query to check
        Returns:
            Query status response
        Raises:
            QueryAPIError: If the API request fails
        """
        response = self.session.get(
            f"{self.config.base_url}/v1/queries/{query_id}",
            timeout=self.config.timeout / 1000
        )
        return self._handle_response(response)

    def get_query_results(
        self,
        query_id: str,
        limit: Optional[int] = None,
        cursor: Optional[str] = None
    ) -> QueryResults:
        """
        Get results of a completed query
        
        Args:
            query_id: ID of the query
            limit: Optional maximum number of results to return
            cursor: Optional pagination cursor
        Returns:
            Paginated query results
        Raises:
            QueryAPIError: If the API request fails
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if cursor is not None:
            params['cursor'] = cursor
            
        url = f"{self.config.base_url}/v1/queries/{query_id}/results"
        if params:
            url = f"{url}?{urlencode(params)}"

        response = self.session.get(url, timeout=self.config.timeout / 1000)
        return self._handle_response(response)

    def wait_for_results(
        self,
        query_id: str,
        timeout: int = 300000,  # 5 minutes default
        poll_interval: int = 1000  # 1 second default
    ) -> QueryResults:
        """
        Wait for a query to complete and return results
        
        Args:
            query_id: ID of the query to wait for
            timeout: Maximum time to wait in milliseconds
            poll_interval: Polling interval in milliseconds
        Returns:
            Query results
        Raises:
            QueryAPIError: If the query fails or times out
        """
        start_time = time.time()
        timeout_seconds = timeout / 1000
        poll_interval_seconds = poll_interval / 1000

        while True:
            status = self.get_query_status(query_id)

            if status['status'] == 'completed':
                return self.get_query_results(query_id)

            if status['status'] == 'failed':
                raise QueryAPIError(
                    f"Query failed: {status.get('error', 'Unknown error')}"
                )

            if time.time() - start_time > timeout_seconds:
                raise QueryAPIError('Query timeout exceeded')

            time.sleep(poll_interval_seconds)

def create_client(config: QueryClientConfig) -> QueryClient:
    """
    Create a new client instance
    
    Args:
        config: Client configuration options
    Returns:
        New QueryClient instance
    """
    return QueryClient(config)

# Package exports
__all__ = ['QueryClient', 'create_client', 'QueryAPIError', 'QueryClientConfig']