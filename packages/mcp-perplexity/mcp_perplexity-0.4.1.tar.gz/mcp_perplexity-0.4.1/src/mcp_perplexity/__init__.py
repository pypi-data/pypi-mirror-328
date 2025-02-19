import asyncio

from . import server


def main():
    """Main entry point for the package."""
    asyncio.run(server.main())


__version__ = "0.4.1"

__all__ = ["main", "server"]
