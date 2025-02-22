import base64
import os
from typing import Dict

import requests

TIDAL_CLIENT_ID = os.getenv("TIDAL_CLIENT_ID")
TIDAL_CLIENT_SECRET = os.getenv("TIDAL_CLIENT_SECRET")


SEARCH_URL = "https://openapi.tidal.com/v2/searchresults"
PLAYLIST_URL = "https://openapi.tidal.com/v2/playlists"


class Client:
    def __init__(self):
        self.token = self._get_access_token()

    def artist_search(self, query: str, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/artists?include=artist&countryCode={country_code}"
        return self._get_response(url, self.token)

    def album_search(self, query: str, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/albums?include=album&countryCode={country_code}"
        return self._get_response(url, self.token)

    def playlist_search(self, query: str, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/playlists?include=playlist&countryCode={country_code}"
        return self._get_response(url, self.token)

    def track_search(self, query: str, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/tracks?include=track&countryCode={country_code}"
        return self._get_response(url, self.token)

    def video_search(self, query: str, country_code: str = "US") -> Dict:
        url = f"{SEARCH_URL}/{query}/relationships/videos?include=video&countryCode={country_code}"
        return self._get_response(url, self.token)

    def top_hit_search(self, query: str, country_code: str = "US") -> Dict:
        includes = "artists,albums,tracks,videos,playlists"
        url = f"{SEARCH_URL}/{query}/relationships/top-hits?include={includes}&countryCode={country_code}"
        return self._get_response(url, self.token)

    def get_playlist(self, playlist_id: str, country_code: str = "US") -> Dict:
        """Get a specific playlist by ID"""
        url = f"{PLAYLIST_URL}/{playlist_id}?countryCode={country_code}"
        return self._get_response(url, self.token)

    def get_user_playlists(self, access_token: str) -> Dict:
        """Get items in a playlist"""
        url = f"{PLAYLIST_URL}/me"
        return self._get_response(url, access_token)

    def _get_access_token(self) -> str:
        credentials = f"{TIDAL_CLIENT_ID}:{TIDAL_CLIENT_SECRET}".encode("utf-8")
        b64_credentials = base64.b64encode(credentials).decode("utf-8")
        url = "https://auth.tidal.com/v1/oauth2/token"
        headers = {"Authorization": f"Basic {b64_credentials}"}
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, headers=headers, data=data)
        return response.json()["access_token"]

    @staticmethod
    def _get_response(url: str, access_token: str) -> Dict:
        headers = {
            "accept": "application/vnd.tidal.v1+json",
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/vnd.tidal.v1+json",
        }
        response = requests.get(url, headers=headers)
        return response.json()
