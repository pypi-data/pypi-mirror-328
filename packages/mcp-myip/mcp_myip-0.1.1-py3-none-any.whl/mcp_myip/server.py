import logging

import httpx
from mcp.server.fastmcp import FastMCP

# Configure logging to console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Create the server
mcp = FastMCP("My IP")


@mcp.tool(name="GetIP", description="Retrieve my IP information from ifconfig.me")
async def get_ip_info() -> str:
    """Get my IP information from ifconfig.me"""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://ifconfig.me/ip")
        return response.text


def run_server():
    import asyncio

    logging.info("Starting FastMCP server...")
    asyncio.run(mcp.run(transport="stdio"))


if __name__ == "__main__":
    run_server()
