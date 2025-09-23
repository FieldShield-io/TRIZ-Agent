"""General-purpose tools for TRIZ Agents.

Provided tools / utilities:
- tavily_tool: web search via Tavily (LangChain community tool)
- wikipedia: Wikipedia search/summarization tool
- arxiv: low-level Arxiv API wrapper (for advanced use or custom tools)
- scrape_webpages(urls): scrape pages with WebBaseLoader (requests + bs4)
- default_answer(): fallback message
- write_document(content, file_name): write a text document to disk
- write_note(content): append a line to project_notes.txt
- read_note(): read contents of project_notes.txt

Notes:
- Tavily requires a TAVILY_API_KEY in your environment for best results.
- `arxiv` here is a utility (not a @tool) so you can build custom chains around it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, List

from langchain_community.document_loaders import WebBaseLoader
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_core.tools import tool

# ---------------------------------------------------------------------
# Third-party search / knowledge tools
# ---------------------------------------------------------------------

# Tavily web search (set TAVILY_API_KEY in env)
tavily_tool = TavilySearch(max_results=5)

# Wikipedia lookup tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Arxiv API helper (utility object, not a LangChain Tool function)
arxiv = ArxivAPIWrapper()

# If you want Google Scholar too, uncomment these lines and ensure credentials if required:
# from langchain_community.tools.google_scholar import GoogleScholarQueryRun
# from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
# google_scholar = GoogleScholarQueryRun(api_wrapper=GoogleScholarAPIWrapper())


# ---------------------------------------------------------------------
# Scraping
# ---------------------------------------------------------------------
@tool
def scrape_webpages(urls: List[str]) -> str:
    """Scrape the provided web pages and return concatenated text with simple tags.

    Uses `WebBaseLoader` (requests + BeautifulSoup under the hood).
    """
    if not urls:
        return "No URLs provided."
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return "\n\n".join(
        [
            f'<Document title="{doc.metadata.get("title", "")}" url="{doc.metadata.get("source", "")}">\n'
            f"{doc.page_content}\n"
            f"</Document>"
            for doc in docs
        ]
    )


# ---------------------------------------------------------------------
# Fallback / defaults
# ---------------------------------------------------------------------
@tool
def default_answer() -> str:
    """Provide a default response when unable to answer."""
    return "I'm sorry, I can't answer that."


# ---------------------------------------------------------------------
# File IO helpers
# ---------------------------------------------------------------------
@tool
def write_document(
    content: Annotated[str, "Text content to be written into the document."],
    file_name: Annotated[str, "Relative file path to save the document (e.g., reports/summary.txt)."],
) -> Annotated[str, "Path of the saved document file."]:
    """Create (and if needed, create parent folders) and save a UTF-8 text document."""
    workdir = Path.cwd()
    dest = workdir / file_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    return f"Document saved to {dest.relative_to(workdir)}"


@tool
def write_note(
    content: Annotated[str, "Text content to be appended to the project note."],
) -> Annotated[str, "Path of the saved note file."]:
    """Append a line to the project notes file (project_notes.txt)."""
    file_name = "project_notes.txt"
    workdir = Path.cwd()
    dest = workdir / file_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("a", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")
    return f"Note saved to {dest.relative_to(workdir)}"


@tool
def read_note() -> Annotated[str, "Content of the note file."]:
    """Read and return the contents of the project notes file."""
    file_name = "project_notes.txt"
    workdir = Path.cwd()
    dest = workdir / file_name
    try:
        return dest.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"No notes found at {dest.relative_to(workdir)}"


__all__ = [
    "tavily_tool",
    "wikipedia",
    "arxiv",
    "scrape_webpages",
    "default_answer",
    "write_document",
    "write_note",
    "read_note",
]
