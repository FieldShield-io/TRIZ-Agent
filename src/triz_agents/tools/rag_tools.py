"""Lightweight RAG tools for TRIZ sources.

Exposes a single LangChain tool:
- rag_triz_tool(question: str) -> str

Design goals:
- Lazy initialization (no heavy work at import time)
- Small, dependency-tolerant (Chroma -> FAISS fallback)
- Clear errors when data or deps are missing
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Sequence

from langchain_core.tools import tool
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Vector stores & loaders
try:
    from langchain_community.vectorstores import Chroma  # preferred
    _HAS_CHROMA = True
except Exception:
    _HAS_CHROMA = False
    Chroma = None  # type: ignore

try:
    from langchain_community.vectorstores import FAISS  # fallback
    _HAS_FAISS = True
except Exception:
    _HAS_FAISS = False
    FAISS = None  # type: ignore

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain import hub
from langchain.prompts import ChatPromptTemplate

from ..llm import get_llm

# -----------------------------
# Configuration
# -----------------------------
# Directory with PDFs to build the TRIZ RAG index from.
# Default: ./triz_books (relative to working directory)
TRIZ_RAG_DIR = Path(os.getenv("TRIZ_RAG_DIR", "triz_books"))

# Chunking defaults
_CHUNK_SIZE = 1000
_CHUNK_OVERLAP = 200

# Lazy singletons
_RETRIEVER = None
_RAG_CHAIN = None


def _load_documents(data_dir: Path) -> Sequence:
    """Load PDF documents from `data_dir` (non-recursive by default)."""
    if not data_dir.exists():
        raise FileNotFoundError(
            f"RAG data directory not found: {data_dir.resolve()}. "
            "Set TRIZ_RAG_DIR env var or create the folder with PDFs."
        )
    loader = DirectoryLoader(
        str(data_dir),
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        use_multithreading=True,
    )
    return loader.load()


def _split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=_CHUNK_SIZE, chunk_overlap=_CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)


def _build_retriever(data_dir: Path):
    """Create a retriever from PDFs in `data_dir` using Chroma or FAISS."""
    docs = _load_documents(data_dir)
    if not docs:
        raise RuntimeError(f"No PDFs found in {data_dir.resolve()} for RAG.")

    splits = _split_documents(docs)
    embeddings = OpenAIEmbeddings()

    # Prefer Chroma if available (no persistence by default)
    if _HAS_CHROMA:
        vs = Chroma.from_documents(
            documents=splits,
            collection_name="triz-rag",
            embedding=embeddings,
        )
        return vs.as_retriever()

    # Fallback to FAISS if chroma not available
    if _HAS_FAISS:
        vs = FAISS.from_documents(splits, embeddings)
        return vs.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # If neither is available, tell the user how to proceed
    raise ImportError(
        "No vector store backend available. Install one of:\n"
        "  - chromadb (for Chroma)  OR\n"
        "  - faiss-cpu (for FAISS)"
    )


def _format_docs(docs) -> str:
    return "\n\n".join(getattr(d, "page_content", "") for d in docs)


def _get_prompt():
    """Pull a standard RAG prompt; fall back to a simple template if hub is unavailable."""
    try:
        return hub.pull("rlm/rag-prompt")
    except Exception:
        return ChatPromptTemplate.from_template(
            "You are a helpful assistant. Use the context to answer.\n\n"
            "Context:\n{context}\n\n"
            "Question: {question}\n\n"
            "Answer concisely and cite relevant snippets."
        )


def _get_rag_chain():
    """Lazily construct and cache the RAG chain."""
    global _RETRIEVER, _RAG_CHAIN
    if _RAG_CHAIN is not None:
        return _RAG_CHAIN

    # Build retriever (can be ~seconds depending on PDF count/size)
    _RETRIEVER = _build_retriever(TRIZ_RAG_DIR)

    prompt = _get_prompt()
    llm = get_llm(model="gpt-4o", temperature=0.0)

    chain = (
        {"context": _RETRIEVER | _format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    _RAG_CHAIN = chain
    return chain


@tool
def rag_triz_tool(question: str) -> str:
    """Search across local TRIZ PDFs and answer the question using RAG.

    Setup:
      - Place relevant PDFs in the directory `TRIZ_RAG_DIR` (default: ./triz_books)
      - Ensure OpenAI API credentials are set for embeddings and chat model.
      - Optionally set TRIZ_RAG_DIR env var to point to your corpus.

    Args:
      question: The user’s query about TRIZ.

    Returns:
      A concise, grounded answer string, or a clear error message.
    """
    try:
        rag_chain = _get_rag_chain()
        return rag_chain.invoke(question)
    except Exception as e:
        return (
            "RAG query failed. Please verify that:\n"
            f"- The directory `{TRIZ_RAG_DIR.resolve()}` exists and contains PDFs\n"
            "- API keys are set (e.g., OPENAI_API_KEY)\n"
            "- A vector store backend is installed (chromadb or faiss-cpu)\n"
            f"Details: {e}"
        )
