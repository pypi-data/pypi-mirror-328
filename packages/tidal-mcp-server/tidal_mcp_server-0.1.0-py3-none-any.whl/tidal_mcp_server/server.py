from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from .client import Client

client = Client()

mcp = FastMCP(
    "tidal", title="TIDAL MPC", description="TIDAL API Model Context Server", version="0.0.1", log_level="DEBUG"
)


@mcp.tool()
async def search(operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Manage search operations using the TIDAL API

    Args:
        operation: The operation to perform. Valid operations:
            Search:
                - artist_search

        params: Dictionary of parameters for the specific operation
    """

    if operation == "artist_search":
        return client.artist_search(
            query=params.get("query", ""),
            access_token=params.get("accessToken", ""),
            limit=params.get("limit", 10),
            country_code=params.get("countryCode", "US"),
        )
    else:
        raise ValueError(f"Unknown operation: {operation}")
