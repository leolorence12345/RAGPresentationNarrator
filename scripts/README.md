# Scripts Directory

Utility scripts for project management and operations.

## Available Scripts

### Setup
- `setup_project.py` - Initialize project structure and directories

### Data Management
- `data/process_presentations.py` - Process presentations and generate metadata
- `data/validate_presentations.py` - Validate presentation files

### Model Management
- `models/save_vector_store.py` - Save FAISS indices and embeddings
- `models/load_vector_store.py` - Load and inspect vector stores

### Cache Management
- `cache/manage_cache.py` - Manage response cache (view, clear, stats)

## Usage

### Setup Project
```bash
python scripts/setup_project.py
```

### Process Presentations
```bash
python data/process_presentations.py
```

### Validate Files
```bash
python data/validate_presentations.py
```

### Manage Cache
```bash
# Show cache statistics
python cache/manage_cache.py stats

# List cache entries
python cache/manage_cache.py list 20

# Clear old cache (older than 7 days)
python cache/manage_cache.py clear 7
```

