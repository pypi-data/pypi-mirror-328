# TIDAL MPC Server

Python implementation of the TIDAL MPC Server using the [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

<img src="https://badge.mcpx.dev?type=server" title="MCP Server"/>

## Features

- [x] Catalogue search

## Usage

To get started you will need a `TIDAL_CLIENT_ID` and `TIDAL_CLIENT_SECRET` for an app registered with TIDAL.
Use the [quick start guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-quick-start) to get started and create your keys

```uv add "mcp[cli]"```

Run the server
```tidal-mcp-server```

Run the server for development
```
source  .venv/bin/activate
mcp dev src/tidal_mcp_server/server.py
```

## Development

This project uses [`uv`] to manage dependencies. Install `uv` following the instructions for your platform.

You can then create a virtual environment and install the dependencies with:

```bash uv sync --all-groups ```

### Linting

This project uses [ruff](https://github.com/charliermarsh/ruff) for linting.

[`uv`]: https://docs.astral.sh/uv/