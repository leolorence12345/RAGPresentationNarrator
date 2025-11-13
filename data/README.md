# Data Directory

This directory contains presentation documents and processed data.

## Structure

```
data/
├── presentations/     # Input presentation files (PDF, PPTX, etc.)
├── processed/         # Processed document chunks (auto-generated, gitignored)
│   ├── chunks/       # Text chunks from documents
│   └── embeddings/   # Generated embeddings
└── metadata/         # Presentation metadata files
    └── presentations_metadata.json
```

## Usage

1. Place your presentation files in `presentations/`
2. Run the pipeline to process documents
3. Processed data will be stored in `processed/` (not tracked in git)
4. Metadata will be generated in `metadata/`

