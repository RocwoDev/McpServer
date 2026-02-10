### MCP Web Utilities Server

Lightweight MCP server that exposes web search and page fetching tools.

#### Features
- `search_on_web` and `search_on_website` using `ddgs` (DDGS | Dux Distributed Global Search, a multi-source search engine).
- `fetch_webpage` that returns simplified Markdown using `crawl4ai` with stealth settings.

#### Requirements
- Python 3.13+
- `uv` installed

Install `uv` on Windows (PowerShell):
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Setup
```
uv sync
```

Then activate the virtual environment and run the crawler setup:
```
.venv\Scripts\activate
crawl4ai-setup
```

#### Run the server
```
uv run src\main.py
```

Or when developing:
```
start_mcp_server.cmd
```

#### Tools
`search_on_web(query: str, results: int = 10) -> str`
- Returns results formatted as:
```
[title](url)
description
```

`search_on_website(query: str, sites: list[str], results: int = 10) -> str`
- Same format, restricted to the provided `sites`.

`fetch_webpage(target_url: str) -> str`
- Returns simplified Markdown for the target page.

#### Tests
```
python -m unittest src.tests
```

#### Notes
- Avoid writing to `STDOUT` (e.g., `print`) when the server is running; it will break JSON RPC communication.
- Network-dependent tests may fail if external services are blocked in the current environment.