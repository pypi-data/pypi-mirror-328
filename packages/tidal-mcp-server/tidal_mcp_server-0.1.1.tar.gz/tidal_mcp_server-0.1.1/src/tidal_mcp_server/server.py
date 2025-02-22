from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from .client import Client

client = Client()

mcp = FastMCP(
    "tidal", title="TIDAL MPC", description="TIDAL API Model Context Server", version="0.1.1", log_level="DEBUG"
)


@mcp.tool()
async def search(operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Manage search operations using the TIDAL API

    Args:
        operation: The operation to perform. Valid operations:
            Search:
                - artist_search
                - album_search
                - playlist_search
                - track_search
                - video_search
                - top_hit_search

        params: Dictionary of parameters for the specific operation
    """
    if operation == "artist_search":
        result = client.artist_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "album_search":
        result = client.album_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "playlist_search":
        result = client.playlist_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "track_search":
        result = client.track_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "video_search":
        result = client.video_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "top_hit_search":
        result = client.top_hit_search(
            query=params.get("query", ""),
            country_code=params.get("countryCode", "US"),
        )
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return result


@mcp.tool()
async def playlist(operation: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Manage playlist operations using the TIDAL API

    Args:
        operation: The operation to perform. Valid operations:
            Playlist:
                - get_playlist
                - get_user_playlists

        params: Dictionary of parameters for the specific operation
    """
    if operation == "get_playlist":
        result = client.get_playlist(
            playlist_id=params.get("playlistId", ""),
            country_code=params.get("countryCode", "US"),
        )
    elif operation == "get_user_playlists":
        result = client.get_user_playlists(
            access_token=params.get("accessToken", ""),
        )
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return result

