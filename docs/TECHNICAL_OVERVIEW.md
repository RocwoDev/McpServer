# Technical Overview

## Project
This project is a Model Context Protocol (MCP) server that exposes web search and webpage fetch tools for MCP clients (e.g., LM Studio). The server uses `FastMCP` and runs with the `stdio` transport.

## Documentation Philosophy
To keep the agent's context clean, this overview is intentionally kept short. It serves as a central hub. Detailed information is modularized into specialized markdown files.  
**Always prefer reading the specific linked file related to your task rather than parsing the whole documentation.**  

## Modules & Workflows
- **Architecture**: Components and data flow: [docs/technical/architecture.md](./technical/architecture.md)

## Project Structure
```text
Project/
├── docs/                      # Technical documentation
├── src/                       # MCP server source code
│   ├── mcp_server.py          # FastMCP server and tool registrations
│   ├── main.py                # Entry point (stdio transport)
│   └── utils/
│       ├── search.py           # DDGS (Dux Distributed Global Search) helpers
│       └── fetch_webpage.py    # Webpage fetch to markdown (crawl4ai)
├── start_mcp_server.cmd       # Convenience script to launch the server
├── AGENTS.md                  # Agent operating guidelines
└── pyproject.toml             # Dependencies and project metadata
```

## Technology Stack
- **Language**: Python 3.13+
- **MCP Server**: `FastMCP` (`mcp` package)
- **Search**: `ddgs` (DDGS | Dux Distributed Global Search, multi-source)
- **Web crawling**: `crawl4ai` (async)
- **Async runtime**: `asyncio`
