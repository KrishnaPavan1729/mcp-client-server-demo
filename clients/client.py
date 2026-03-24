import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters 
from loguru import logger 

logger.add("logs/simple_client.log")


async def main():
    server_params = StdioServerParameters(command="python", args=["servers/server.py"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("add", {"a": 5, "b": 7})
            logger.info(result)

asyncio.run(main())