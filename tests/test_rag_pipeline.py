"""
Tests for RAG Pipeline
"""

import pytest
from src.pipeline.rag_pipeline import RAGPipeline


def test_pipeline_initialization():
    """Test RAG pipeline initialization."""
    pipeline = RAGPipeline(
        documents_path="data/presentations/",
        cache_enabled=True
    )
    assert pipeline.cache_enabled is True
    assert pipeline.vector_store_type == "faiss"


def test_retrieve_context():
    """Test context retrieval."""
    pipeline = RAGPipeline()
    context = pipeline.retrieve_context("test query", k=5)
    assert isinstance(context, list)


def test_generate_narrative():
    """Test narrative generation."""
    pipeline = RAGPipeline()
    narrative = pipeline.generate_narrative("test query")
    assert isinstance(narrative, str)
    assert len(narrative) > 0

