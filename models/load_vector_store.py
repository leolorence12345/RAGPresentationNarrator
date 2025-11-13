"""
Utility script to load and inspect FAISS vector store.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.save_vector_store import VectorStoreManager
import faiss


def inspect_index(index_path: str = "models/faiss_index.index"):
    """
    Inspect a FAISS index file.
    
    Args:
        index_path: Path to FAISS index file
    """
    index_file = Path(index_path)
    
    if not index_file.exists():
        print(f"✗ Index file not found: {index_path}")
        return
    
    try:
        # Load index
        index = faiss.read_index(str(index_file))
        
        print("=" * 60)
        print("FAISS Index Information")
        print("=" * 60)
        print(f"File: {index_path}")
        print(f"Size: {index_file.stat().st_size / 1024 / 1024:.2f} MB")
        print(f"Type: {type(index).__name__}")
        print(f"Dimension: {index.d}")
        print(f"Total vectors: {index.ntotal}")
        print(f"Is trained: {index.is_trained}")
        
        if hasattr(index, 'metric_type'):
            metric_names = {
                faiss.METRIC_INNER_PRODUCT: "Inner Product",
                faiss.METRIC_L2: "L2 (Euclidean)"
            }
            metric = metric_names.get(index.metric_type, f"Unknown ({index.metric_type})")
            print(f"Metric: {metric}")
        
        print("=" * 60)
        
    except Exception as e:
        print(f"✗ Error loading index: {e}")


if __name__ == "__main__":
    manager = VectorStoreManager()
    
    print("Available model files:")
    manager.list_models()
    print()
    
    # Try to inspect default index
    inspect_index()

