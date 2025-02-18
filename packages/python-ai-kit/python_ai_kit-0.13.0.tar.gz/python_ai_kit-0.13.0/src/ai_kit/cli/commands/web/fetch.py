from ai_kit.core.web.fetcher import Fetcher
from ai_kit.core.web.parser import extract_internal_links, gemini_html_to_markdown, html_to_markdown
from ai_kit.utils import print_stream
from ai_kit.shared_console import shared_console, shared_error_console
from ai_kit.core.web.duckduckgo import DuckDuckGoSearch
from typing import Optional, Set, Dict
import aiohttp
from urllib.parse import urlparse
from rich.table import Table

def clean_url(url: str):
    if url.startswith("http") or url.startswith("https"):
        return url
    elif url.startswith("www."):
        return f"https://{url}"
    else:
        return url

async def get_page_snippets(base_url: str) -> Dict[str, str]:
    """Get snippets for pages on the domain using DuckDuckGo site search."""
    base_domain = urlparse(base_url).netloc
    ddg = DuckDuckGoSearch()
    
    # Search for pages on this domain
    results = await ddg.search(f"site:{base_domain}")
    
    # Create a mapping of URLs to their snippets
    snippets = {}
    for result in results:
        snippets[result["href"]] = result["body"]
    
    return snippets


async def display_links_table(links: Set[str], base_url: str, status):
    """Display internal links in a formatted table."""
    # Get snippets for the domain
    status.update("[bold green]Fetching page descriptions...[/bold green]")
    snippets = await get_page_snippets(base_url)

    # Filter links to only those with snippets
    links_with_snippets = {
        link for link in links 
        if link in snippets or link.rstrip('/') in snippets
    }

    if not links_with_snippets:
        return

    table = Table(title=f"\nRelevant Internal Pages Found on {base_url}")
    table.add_column("Path", style="cyan", no_wrap=True)
    table.add_column("Description", style="white", max_width=60)
    table.add_column("Full URL", style="blue", no_wrap=True)

    # Sort links for consistent display
    sorted_links = sorted(links_with_snippets)

    for link in sorted_links:
        parsed = urlparse(link)
        # Get relative path, or use '/' for homepage
        path = parsed.path or '/'
        if parsed.query:
            path += f"?{parsed.query}"
            
        # Get snippet if available
        snippet = snippets.get(link, "")
        if not snippet and link.rstrip('/') in snippets:
            # Try without trailing slash
            snippet = snippets.get(link.rstrip('/'), "")
            
        table.add_row(path, snippet, link)

    shared_console.print(table)


async def fetch_web(url: str, no_links_table: bool = False) -> Optional[int]:
    """Fetch and convert a webpage to markdown.
    
    Args:
        url: The URL to fetch
        raw: If True, skips the Gemini cleaning step
        no_links_table: If True, skips displaying the internal links table
    """
    url = clean_url(url)
    try:
        async with Fetcher() as fetcher:
            with shared_console.status("[bold green]Fetching content...[/bold green]") as status:
                try:
                    results = await fetcher.batch_fetch([url])
                except aiohttp.ClientResponseError as e:
                    if e.status == 403:
                        shared_error_console.print(
                            "[red]Error 403: Access Forbidden[/red]\n"
                            "This usually means:\n"
                            "1. The website is blocking automated access\n"
                            "2. You might need authentication\n"
                            "3. The website's robots.txt may be restricting access\n"
                            f"Try opening {url} in a regular web browser instead."
                        )
                        return 1
                    raise  # Re-raise other HTTP errors

                if not results or not results[0]:
                    shared_error_console.print(f"[red]Error: Could not fetch content from {url}[/red]")
                    return 1

                # Extract internal links before cleaning HTML
                internal_links = extract_internal_links(results[0], url)

                # Convert the cleaned HTML to markdown with no link syntax
                raw_markdown = html_to_markdown(results[0], no_links=True)

                status.update("[bold green]Cleaning content with Gemini...[/bold green]")
                stream = await gemini_html_to_markdown(raw_markdown)
                # Print the formatted markdown with syntax highlighting
                shared_console.print(f"\n[bold blue]Content from {url}:[/bold blue]\n")
                await print_stream(stream)

                # Display internal links table after content if requested
                if internal_links and not no_links_table:
                    await display_links_table(internal_links, url, status)

            return 0
    except Exception as e:
        shared_error_console.print(f"[red]Error fetching page: {str(e)}[/red]")
        return 1