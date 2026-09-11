
from fastmcp import FastMCP
import random
import json

mcp = FastMCP("simple calculator")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together and return the result.

    Args:
        a: first number
        b: second number

    Returns:
        Sum of a and b.
    """
    return a + b


@mcp.tool
def random_number(a: int, b: int) -> int:
    """Return a random number between a and b.

    Args:
        a: first number
        b: second number

    Returns:
        Random number between a and b.
    """
    return random.randint(a, b)


@mcp.resource("info://server")
def server_info() -> str:
    """Return server info about the server."""

    info = {
        "name": "simple calculator",
        "version": "1.0.0",
        "description": "A simple calculator tool",
        "tools": ["add", "random_number"],
        "author": "Deepanshu",
        "contact": "deepanshu.jain@gmail.com"
    }

    return json.dumps(info, indent=4)


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
