# server/server.py

from mcp.server.fastmcp import FastMCP
from loguru import logger

logger.add("logs/simple_server.log")

mcp = FastMCP("Simple MCP server")

@mcp.tool()
async def add(a: int, b: int) -> int:
    logger.info(f"Adding {a} + {b}")
    return a + b

if __name__ == "__main__":
    mcp.run()