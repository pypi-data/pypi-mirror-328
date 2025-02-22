import argparse

from .server import mcp


def main():
    parser = argparse.ArgumentParser(description="Provides access to TIDAL API functionality through MCP.")
    parser.parse_args()
    mcp.run()


if __name__ == "__main__":
    main()
