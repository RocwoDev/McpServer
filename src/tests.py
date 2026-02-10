import asyncio
import unittest

from src.utils.fetch_webpage import ERROR_EMPTY_URL, ERROR_EVENT_LOOP_PREFIX
from src.mcp_server import fetch_webpage, search_on_web


class MyTestCase(unittest.TestCase):
    def assert_search_result(self, result: str):
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "No results found")
        if result.startswith("Error:"):
            self.fail(f"Search error returned: {result}")

    def test_search(self):
        result = search_on_web("python async await httpx requests examples", results=25)
        self.assert_search_result(result)

    def test_search_github_only(self):
        result = search_on_web("site:github.com fastmcp python example", results=20)
        self.assert_search_result(result)

    def test_fetch_webpage_empty_url(self):
        result = fetch_webpage("   ")
        self.assertEqual(result, ERROR_EMPTY_URL)

    def test_fetch_webpage_event_loop_error(self):
        async def call_fetch():
            return fetch_webpage("https://example.com")

        result = asyncio.run(call_fetch())
        self.assertTrue(result.startswith(ERROR_EVENT_LOOP_PREFIX))

    def test_fetch_webpage_markdown_example(self):
        result = fetch_webpage("https://example.com/")
        self.assertIsInstance(result, str)
        self.assertTrue(result.strip())
        self.assertIn("Example Domain", result)


if __name__ == '__main__':
    unittest.main()
