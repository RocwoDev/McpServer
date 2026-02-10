from mcp.server.fastmcp import FastMCP

from utils.fetch_webpage import fetch_webpage_markdown
from utils.search import _search_on_web, _build_site_query

# Initialize FastMCP server
mcp = FastMCP("McpServer")

@mcp.prompt()
def clever_agent_instructions() -> str:
    return """
**Mandatory pipeline:**

1. Understand the user's question completely.  
2. If unsure about any word, term, acronym, name or concept → immediately web-search each unclear term (1 query per term).  
3. Perform ALL searches in English by default (largest volume of quality results).  
   Only switch to another language when you judge it clearly necessary for accuracy or relevance.  
4. Once question is 100% clear → perform main web search to answer it.  
5. From search results → open/fetch the most promising pages one by one to read full content.  
6. With this information → give precise final answer.  
7. If still no satisfactory answer → say "I couldn't find it" + ask 1–2 targeted clarifying questions.
    """

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
async def fetch_webpage(target_url: str) -> str:
    """
    Fetches a webpage and returns a simplified markdown representation.
    """
    return await fetch_webpage_markdown(target_url)


