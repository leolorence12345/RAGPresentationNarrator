# Models Directory

This directory stores FAISS vector indices and model artifacts.

## Contents

- **FAISS Index**: Vector store index file (`.index`)
- **Embeddings**: Pre-computed embeddings (`.pkl`)
- **Vector Store**: Serialized vector store objects

## Note

Model files are generated automatically when you:
1. Load documents into the pipeline
2. Create the vector store
3. Process embeddings

These files are typically large and may be gitignored. Keep backups of important indices.

