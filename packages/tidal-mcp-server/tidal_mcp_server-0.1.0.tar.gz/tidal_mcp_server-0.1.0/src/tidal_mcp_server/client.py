import base64
import os
from typing import Dict

import requests
from mcp import ErrorData, McpError
from mcp.types import INVALID_PARAMS

SEARCH_URL = "https://openapi.tidal.com/v2/searchresults"


class Client:

    def artist_search(self, query: str, access_token: str, limit=10, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/artists?include=artist&countryCode={country_code}"

        headers = {
            "accept": "application/vnd.tidal.v1+json",
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/vnd.tidal.v1+json",
        }

        response = requests.get(url, headers=headers)

        # TODO: Limit the number of results

        return response.json()