import asyncio
import unittest

from tidal_mcp_server.server import search


class TestServer(unittest.TestCase):
    def test_search_invalid_operation(self):
        operation = "invalid_operation"
        params = {"query": "eminem"}

        with self.assertRaises(ValueError):
            asyncio.run(search(operation, params))
