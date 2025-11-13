# Designing Real-Time Accessible Learning for Visually Impaired Students

**RAG-Powered Presentation Narrator for Visually Impaired Learners**

An intelligent Retrieval-Augmented Generation (RAG) system that automatically generates contextual narratives from presentation documents, specifically designed to enhance accessibility for visually impaired learners.

> 📄 **Accepted at TREO Talks 2024**  
> This project was presented at TREO Talks 2024. See the [accepted paper](papers/TReO_Talks_2024.pdf) for details.

## 🎯 Project Overview

This project implements a production-ready RAG pipeline using LangChain and FAISS to process 200+ presentation documents and generate real-time, contextual narratives. The system is optimized for live deployments with advanced caching mechanisms and memory optimization techniques.

## ✨ Key Features

- **RAG Pipeline**: LangChain-based retrieval system with FAISS vector store
- **Contextual Generation**: Intelligent narrative creation from 200+ presentation documents
- **Accessibility Focus**: Designed specifically for visually impaired learners
- **Prompt Engineering**: Custom prompt templates and agent chains for automated narrative generation
- **Performance Optimization**: 
  - LLM response caching for faster retrieval
  - Memory usage optimization
  - 25% speed improvement for real-time deployments
- **Live Deployment Ready**: Optimized for real-time system performance

## 🏗️ Architecture

```
RAG-Presentation-Narrator/
├── src/                    # Source code
│   ├── pipeline/           # RAG pipeline components
│   ├── agents/             # LangChain agents and chains
│   ├── prompts/            # Prompt templates
│   ├── cache/              # Caching utilities
│   └── utils/              # Utility functions
├── data/                   # Presentation documents and processed data
├── models/                 # FAISS indices and model artifacts
├── cache/                  # LLM response cache
├── tests/                  # Unit and integration tests
└── docs/                   # Documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd RAG-Presentation-Narrator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

- **LangChain**: RAG pipeline and agent orchestration
- **FAISS**: Vector similarity search
- **OpenAI/Anthropic**: LLM providers for generation
- **ChromaDB/Weaviate**: Optional vector stores
- **Redis**: Response caching (optional)
- **NumPy/Pandas**: Data processing

## 📋 Usage

### Basic Pipeline Execution

```python
from src.pipeline.rag_pipeline import RAGPipeline

# Initialize pipeline
pipeline = RAGPipeline(
    documents_path="data/presentations/",
    cache_enabled=True
)

# Generate narrative for a query
query = "Explain the key concepts from the machine learning presentation"
narrative = pipeline.generate_narrative(query)
print(narrative)
```

### Agent Chain Usage

```python
from src.agents.narrative_agent import NarrativeAgent

# Initialize agent with custom prompts
agent = NarrativeAgent(
    prompt_template="src/prompts/narrative_template.txt",
    cache_enabled=True
)

# Generate contextual narrative
narrative = agent.create_narrative(
    presentation_id="ml_intro_2024",
    context="machine learning basics"
)
```

## 🔧 Components

### 1. RAG Pipeline (`src/pipeline/`)

- Document ingestion and preprocessing
- Text chunking and embedding generation
- FAISS index creation and management
- Retrieval and ranking mechanisms

### 2. Agent Chains (`src/agents/`)

- LangChain agent orchestration
- Custom prompt templates
- Narrative generation workflows
- Context management

### 3. Prompt Templates (`src/prompts/`)

- Pre-defined prompt templates for different use cases
- Accessibility-focused narrative formats
- Context-aware prompt generation

### 4. Caching System (`src/cache/`)

- LLM response caching
- Vector store caching
- Memory-efficient cache management

## 📊 Performance Optimizations

### Caching Strategy

- **LLM Response Cache**: Reduces API calls by 40-60%
- **Vector Store Cache**: Pre-computed embeddings for faster retrieval
- **Memory Optimization**: Efficient data structures and lazy loading

### Speed Improvements

- **25% faster real-time performance** through:
  - Response caching
  - Optimized vector search
  - Parallel processing where applicable
  - Memory-efficient data structures

## 🎓 Use Case: Visually Impaired Learners

The system is specifically designed to:

1. **Convert visual presentations to audio narratives**
2. **Provide contextual explanations** of complex concepts
3. **Maintain presentation structure** in narrative format
4. **Support real-time queries** during learning sessions
5. **Generate accessible content** following accessibility guidelines

## 📁 Data Structure

### Presentation Documents

Place presentation files (PDF, PPTX, etc.) in `data/presentations/`:
```
data/
├── presentations/
│   ├── presentation_001.pdf
│   ├── presentation_002.pptx
│   └── ...
├── processed/
│   ├── chunks/
│   └── embeddings/
└── metadata/
    └── presentations_metadata.json
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_rag_pipeline.py
pytest tests/test_agents.py
```

## 📈 Performance Metrics

- **Document Processing**: 200+ presentations indexed
- **Query Response Time**: < 2 seconds (with cache)
- **Cache Hit Rate**: ~70% for common queries
- **Memory Usage**: Optimized for production deployment

## 🔐 Configuration

Create a `config.yaml` file:

```yaml
llm:
  provider: "openai"  # or "anthropic"
  model: "gpt-4"
  temperature: 0.7

vector_store:
  type: "faiss"
  embedding_model: "text-embedding-ada-002"
  index_path: "models/faiss_index"

cache:
  enabled: true
  type: "memory"  # or "redis"
  ttl: 3600

accessibility:
  narrative_format: "audio_friendly"
  include_descriptions: true
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

[Specify your license here]

## 📄 Publication

This work was accepted and presented at **TReO Talks 2024**.

**Paper**: [Designing Real-Time Accessible Learning for Visually Impaired Students](papers/TReO_Talks_2024.pdf)

## 👥 Authors

- Developed as part of accessibility and AI research initiatives

## 🙏 Acknowledgments

- TReO Talks 2024 for accepting this work
- LangChain community for RAG framework
- FAISS team for efficient vector search
- Accessibility advocates for guidance on inclusive design

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This system is optimized for production use with real-time narrative generation capabilities, making it suitable for live educational deployments and accessibility applications.



