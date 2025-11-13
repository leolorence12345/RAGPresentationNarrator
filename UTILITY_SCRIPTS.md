# Utility Scripts Added

This document lists all the utility scripts added to support the project directories.

## 📁 Data Directory Scripts

### `data/process_presentations.py`
**Purpose**: Process presentations and generate metadata

**Features**:
- Scans `data/presentations/` directory for PDF/PPTX files
- Generates metadata JSON file with file information
- Validates directory structure
- Creates missing directories automatically

**Usage**:
```bash
python data/process_presentations.py
```

### `data/validate_presentations.py`
**Purpose**: Validate presentation files

**Features**:
- Checks if files are readable
- Validates file formats (PDF, PPTX)
- Tests text extraction
- Reports validation results

**Usage**:
```bash
python data/validate_presentations.py
```

## 📁 Models Directory Scripts

### `models/save_vector_store.py`
**Purpose**: Save and manage FAISS vector stores

**Features**:
- `VectorStoreManager` class for saving/loading FAISS indices
- Save embeddings as pickle files
- Save metadata alongside indices
- List all model files

**Usage**:
```python
from models.save_vector_store import VectorStoreManager

manager = VectorStoreManager()
manager.save_faiss_index(index, "my_index")
manager.list_models()
```

### `models/load_vector_store.py`
**Purpose**: Load and inspect FAISS vector stores

**Features**:
- Load FAISS indices from disk
- Inspect index properties (dimension, size, metric type)
- Display index information

**Usage**:
```bash
python models/load_vector_store.py
```

## 📁 Cache Directory Scripts

### `cache/manage_cache.py`
**Purpose**: Manage response cache

**Features**:
- View cache statistics (size, file count)
- List cache entries
- Clear cache (all or by age)
- Show cache information

**Usage**:
```bash
# Show statistics
python cache/manage_cache.py stats

# List entries
python cache/manage_cache.py list 20

# Clear old cache (older than 7 days)
python cache/manage_cache.py clear 7
```

## 📁 Scripts Directory

### `scripts/setup_project.py`
**Purpose**: Initialize project structure

**Features**:
- Creates all necessary directories
- Generates initial metadata file
- Creates config.yaml from example
- Verifies project structure

**Usage**:
```bash
python scripts/setup_project.py
```

## Summary

All utility scripts are designed to:
- ✅ Work with the existing project structure
- ✅ Handle missing directories gracefully
- ✅ Provide clear error messages
- ✅ Include proper documentation
- ✅ Use relative paths from project root

These scripts support the functionality described in the README files for each directory.

