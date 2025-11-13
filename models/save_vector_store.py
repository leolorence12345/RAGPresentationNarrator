"""
Utility script to save and manage FAISS vector store.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pickle
from typing import Optional
import faiss
import numpy as np


class VectorStoreManager:
    """Manager for saving and loading FAISS vector stores."""
    
    def __init__(self, models_dir: str = "models"):
        """
        Initialize vector store manager.
        
        Args:
            models_dir: Directory to store model files
        """
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(parents=True, exist_ok=True)
    
    def save_faiss_index(
        self,
        index: faiss.Index,
        index_name: str = "faiss_index",
        metadata: Optional[dict] = None
    ) -> Path:
        """
        Save FAISS index to disk.
        
        Args:
            index: FAISS index object
            index_name: Name for the index file (without extension)
            metadata: Optional metadata to save alongside index
            
        Returns:
            Path to saved index file
        """
        index_path = self.models_dir / f"{index_name}.index"
        
        # Save FAISS index
        faiss.write_index(index, str(index_path))
        print(f"✓ Saved FAISS index to {index_path}")
        
        # Save metadata if provided
        if metadata:
            metadata_path = self.models_dir / f"{index_name}_metadata.pkl"
            with open(metadata_path, 'wb') as f:
                pickle.dump(metadata, f)
            print(f"✓ Saved metadata to {metadata_path}")
        
        return index_path
    
    def load_faiss_index(
        self,
        index_name: str = "faiss_index"
    ) -> tuple[faiss.Index, Optional[dict]]:
        """
        Load FAISS index from disk.
        
        Args:
            index_name: Name of the index file (without extension)
            
        Returns:
            Tuple of (FAISS index, metadata if available)
        """
        index_path = self.models_dir / f"{index_name}.index"
        
        if not index_path.exists():
            raise FileNotFoundError(f"Index file not found: {index_path}")
        
        # Load FAISS index
        index = faiss.read_index(str(index_path))
        print(f"✓ Loaded FAISS index from {index_path}")
        
        # Load metadata if available
        metadata_path = self.models_dir / f"{index_name}_metadata.pkl"
        metadata = None
        if metadata_path.exists():
            with open(metadata_path, 'rb') as f:
                metadata = pickle.load(f)
            print(f"✓ Loaded metadata from {metadata_path}")
        
        return index, metadata
    
    def save_embeddings(
        self,
        embeddings: np.ndarray,
        embeddings_name: str = "embeddings"
    ) -> Path:
        """
        Save embeddings array to disk.
        
        Args:
            embeddings: Numpy array of embeddings
            embeddings_name: Name for the embeddings file (without extension)
            
        Returns:
            Path to saved embeddings file
        """
        embeddings_path = self.models_dir / f"{embeddings_name}.pkl"
        
        with open(embeddings_path, 'wb') as f:
            pickle.dump(embeddings, f)
        
        print(f"✓ Saved embeddings to {embeddings_path}")
        print(f"  Shape: {embeddings.shape}, Size: {embeddings.nbytes / 1024 / 1024:.2f} MB")
        
        return embeddings_path
    
    def load_embeddings(self, embeddings_name: str = "embeddings") -> np.ndarray:
        """
        Load embeddings array from disk.
        
        Args:
            embeddings_name: Name of the embeddings file (without extension)
            
        Returns:
            Numpy array of embeddings
        """
        embeddings_path = self.models_dir / f"{embeddings_name}.pkl"
        
        if not embeddings_path.exists():
            raise FileNotFoundError(f"Embeddings file not found: {embeddings_path}")
        
        with open(embeddings_path, 'rb') as f:
            embeddings = pickle.load(f)
        
        print(f"✓ Loaded embeddings from {embeddings_path}")
        print(f"  Shape: {embeddings.shape}")
        
        return embeddings
    
    def list_models(self):
        """List all model files in the models directory."""
        print("=" * 60)
        print("Model Files")
        print("=" * 60)
        
        model_files = list(self.models_dir.glob("*"))
        
        if not model_files:
            print("No model files found")
            return
        
        for file_path in sorted(model_files):
            if file_path.is_file():
                size_mb = file_path.stat().st_size / 1024 / 1024
                print(f"  {file_path.name:40s} {size_mb:8.2f} MB")
        
        print("=" * 60)


if __name__ == "__main__":
    manager = VectorStoreManager()
    manager.list_models()

