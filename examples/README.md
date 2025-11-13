# Examples

This directory contains example scripts demonstrating how to use the RAG Presentation Narrator.

## Files

- `example_usage.py` - Basic usage examples for pipeline and agent

## Running Examples

```bash
# Make sure you have:
# 1. Installed dependencies: pip install -r requirements.txt
# 2. Created config.yaml from config.yaml.example
# 3. Added API keys to config.yaml
# 4. Added presentation files to data/presentations/

# Run the example
python examples/example_usage.py
```

## Example Workflows

### Basic Pipeline
1. Initialize pipeline
2. Load documents
3. Create vector store
4. Generate narratives

### Agent Usage
1. Initialize agent with prompt template
2. Generate contextual narratives
3. Use caching for performance

