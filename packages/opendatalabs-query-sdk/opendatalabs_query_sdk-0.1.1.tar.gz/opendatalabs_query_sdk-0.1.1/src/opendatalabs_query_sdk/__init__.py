# src/query_api_sdk/__init__.py
from .client import (
    QueryClient,
    create_client,
    QueryAPIError,
    QueryClientConfig,
)

__version__ = "0.1.0"

__all__ = [
    "QueryClient",
    "create_client", 
    "QueryAPIError",
    "QueryClientConfig",
]