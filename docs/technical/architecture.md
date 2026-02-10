# MCP Server Architecture

## Overview
The project is a single FastMCP server that exposes tools over the MCP `stdio` transport. A client (e.g., LM Studio) launches the process and communicates via `stdin`/`stdout`.

## Components
- **Server** (`src/mcp_server.py`): Creates the `FastMCP` instance and registers tools.
- **Entry point** (`src/main.py`): Starts the server with `mcp.run(transport="stdio")`.
- **Search utilities** (`src/utils/search.py`): Uses `ddgs` (DDGS | Dux Distributed Global Search) to fetch multi-source web search results and formats them.
- **Webpage fetch** (`src/utils/fetch_webpage.py`): Uses `crawl4ai` with an async crawler and returns markdown.

## Data Flow
1. MCP client starts the server process (e.g., via `start_mcp_server.cmd`).
2. Client calls a tool (`search_on_web`, `search_on_website`, `fetch_webpage`).
3. The tool delegates to helper modules and returns a formatted string result to the client.

## Notes
- The transport is `stdio`, so each process serves a single client instance.
- Network access occurs inside `ddgs` and `crawl4ai` utilities.
- `ddgs` is a multi-source search engine (DDGS | Dux Distributed Global Search), so results may originate from multiple sites.
