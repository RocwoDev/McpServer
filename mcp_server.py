from mcp.server.fastmcp import FastMCP

from fetch_webpage_utils import fetch_webpage_markdown
from search_utils import _search_on_web, _build_site_query

# Initialize FastMCP server
mcp = FastMCP("McpServer")

@mcp.tool()
def search_on_web(query: str, results: int = 10) -> str:
    """
    Searches the web for information related to the given query.\n
    Return format :\n
    [result 1 title](url)\n
    result 1 description\n
    [result 2 title](url)\n
    result 2 description\n
    ...
    """
    return _search_on_web(query, results=results)


@mcp.tool()
def search_on_website(query: str, sites: list[str], results: int = 10) -> str:
    """
    Searches the web for information related to the given query, restricted to specific sites.\n
    Return format :\n
    [result 1 title](url)\n
    result 1 description\n
    [result 2 title](url)\n
    result 2 description\n
    ...
    """
    site_query = _build_site_query(query, sites)
    return _search_on_web(site_query, results=results)


@mcp.tool()
def fetch_webpage(target_url: str) -> str:
    """
    Fetches a webpage and returns a simplified markdown representation.
    """
    return fetch_webpage_markdown(target_url)


