import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


ERROR_EMPTY_URL = "Error: Empty url"
ERROR_CRAWL_FAILED_PREFIX = "Error: Unable to fetch webpage"
ERROR_EVENT_LOOP_PREFIX = "Error: Unable to run crawler"


_BROWSER_CONFIG = BrowserConfig(
    headless=True,
    enable_stealth=True,
    browser_type="chromium",
)
_RUN_CONFIG = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    word_count_threshold=10,
    remove_overlay_elements=True,
)


async def _crawl_to_markdown(target_url: str) -> str:
    async with AsyncWebCrawler(config=_BROWSER_CONFIG) as crawler:
        result = await crawler.arun(url=target_url, config=_RUN_CONFIG)
    if result.success:
        return result.markdown
    return f"{ERROR_CRAWL_FAILED_PREFIX}: {result.error_message}"


def fetch_webpage_markdown(target_url: str) -> str:
    if not target_url or not target_url.strip():
        return ERROR_EMPTY_URL
    try:
        return asyncio.run(_crawl_to_markdown(target_url))
    except RuntimeError as exc:
        return f"{ERROR_EVENT_LOOP_PREFIX}: {exc}"