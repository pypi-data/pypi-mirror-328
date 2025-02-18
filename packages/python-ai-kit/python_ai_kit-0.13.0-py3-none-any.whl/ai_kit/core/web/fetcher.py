from ai_kit.shared_console import shared_console
from ai_kit.core.llms.google_genai_client import GoogleGenAI
from urllib.parse import urlparse, urljoin
import aiohttp
import markdownify
import asyncio
from bs4 import BeautifulSoup
from typing import TypedDict, Set, AsyncIterator
from ai_kit.core.web.parser import html_to_markdown
class FetcherResult(TypedDict):
    title: str
    href: str
    snippet: str
    parsed_page_content: str

class Fetcher:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.124 Safari/537.36"
        }
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def _fetch_page(self, url: str) -> str:
        try:
            async with self.session.get(url, timeout=10) as response:
                response.raise_for_status()  # This will raise ClientResponseError
                return await response.text()
        except aiohttp.ClientResponseError as e:
            raise  # Re-raise to be handled by caller
        except Exception as e:
            shared_console.print(f"[red]Error fetching page: {e}[/red]")
            return ""
    
    async def batch_fetch(self, urls: list[str]) -> list[str]:
        return await asyncio.gather(*[self._fetch_page(url) for url in urls])
    

    async def batch_fetch_and_parse_pages(self, results: list[dict]) -> list[str]:
        async def _task(result: dict) -> str:
            html = await self._fetch_page(result["href"])
            parsed_page_content = html_to_markdown(html)
            
            return {
                "title": result["title"],
                "href": result["href"],
                "snippet": result["body"],
                "parsed_page_content": parsed_page_content,
            }

        return await asyncio.gather(*[_task(result) for result in results])
