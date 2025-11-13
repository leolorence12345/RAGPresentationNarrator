# Usage Guide

## Quick Start

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Copy configuration
cp config.yaml.example config.yaml

# Edit config.yaml with your API keys
```

### 2. Add Presentations

Place your presentation files in `data/presentations/`:
- PDF files (`.pdf`)
- PowerPoint files (`.pptx`)

### 3. Initialize Pipeline

```python
from src.pipeline.rag_pipeline import RAGPipeline

pipeline = RAGPipeline(
    documents_path="data/presentations/",
    cache_enabled=True
)
```

### 4. Process Documents

```python
# Load and process documents
documents = pipeline.load_documents()
pipeline.create_vector_store(documents)
```

### 5. Generate Narratives

```python
# Generate narrative for a query
query = "Explain the key concepts from the machine learning presentation"
narrative = pipeline.generate_narrative(query)
print(narrative)
```

## Advanced Usage

### Using the Agent

```python
from src.agents.narrative_agent import NarrativeAgent

agent = NarrativeAgent(
    prompt_template="src/prompts/narrative_template.txt",
    cache_enabled=True
)

narrative = agent.create_narrative(
    presentation_id="ml_intro_2024",
    context="machine learning basics"
)
```

### Custom Configuration

Edit `config.yaml` to customize:
- LLM provider and model
- Vector store settings
- Cache configuration
- Accessibility options

## Troubleshooting

### Common Issues

1. **No documents found**: Check `data/presentations/` directory
2. **API errors**: Verify API keys in `config.yaml`
3. **Memory issues**: Reduce batch size in config
4. **Slow performance**: Enable caching and check cache settings

