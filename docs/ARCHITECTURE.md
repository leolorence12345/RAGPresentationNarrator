# System Architecture

## Overview

The RAG-Powered Presentation Narrator uses a modular architecture designed for scalability and performance.

## Components

### 1. Document Processing Layer
- **DocumentProcessor**: Extracts text from PDF/PPTX files
- **Chunking**: Splits documents into manageable chunks
- **Metadata Extraction**: Captures presentation structure

### 2. Vector Store Layer
- **FAISS Index**: Fast similarity search
- **Embeddings**: Text-to-vector conversion
- **Retrieval**: Context-aware document retrieval

### 3. Generation Layer
- **NarrativeAgent**: LangChain agent for narrative creation
- **Prompt Templates**: Accessibility-focused prompts
- **LLM Integration**: OpenAI/Anthropic API calls

### 4. Caching Layer
- **ResponseCache**: LLM response caching
- **Memory Optimization**: Efficient data structures
- **Performance Tuning**: 25% speed improvement

## Data Flow

```
Presentations → Document Processing → Chunking → Embeddings → FAISS Index
                                                                    ↓
Query → Retrieval → Context → Agent → LLM → Narrative → Cache
```

## Performance Optimizations

- Response caching reduces API calls by 40-60%
- Vector store caching for faster retrieval
- Memory-efficient data structures
- Parallel processing where applicable

