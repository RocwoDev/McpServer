from ddgs import DDGS
ERROR_EMPTY_QUERY = "Error: Empty query"
ERROR_INVALID_RESULTS = "Error: Invalid results count"
ERROR_HTTP_STATUS_PREFIX = "Error: Unable to fetch search results"
ERROR_NO_RESULTS_PARSED = "Error: No results parsed"


def _search_on_web(query: str, results: int = 10) -> str:
    if not query or not query.strip():
        return ERROR_EMPTY_QUERY
    if results <= 0:
        return ERROR_INVALID_RESULTS
    try:
        with DDGS() as ddgs:
            page_results = list(ddgs.text(query, max_results=results))
    except Exception as exc:
        return f"{ERROR_HTTP_STATUS_PREFIX}: {exc}"
    if not page_results:
        return ERROR_NO_RESULTS_PARSED

    formatted = []
    for item in page_results:
        title = (item.get("title") or "").strip()
        url = (item.get("href") or item.get("url") or "").strip()
        description = (item.get("body") or item.get("snippet") or "").strip()
        if not title or not url:
            continue
        formatted.append(f"[{title}]({url})\n{description}")
    if not formatted:
        return ERROR_NO_RESULTS_PARSED

    return "\n".join(formatted)


def _build_site_query(query: str, sites: list[str]) -> str:
    cleaned_sites = [site.strip() for site in sites if site.strip()]
    if not cleaned_sites:
        return query
    site_filter = " OR ".join(f"site:{site}" for site in cleaned_sites)
    return f"{query} ({site_filter})"
