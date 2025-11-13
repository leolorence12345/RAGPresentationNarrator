"""
Utility script to process presentations and generate metadata.
Run this script to scan the presentations directory and create metadata.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import json
import os
from datetime import datetime
from typing import List, Dict
from src.utils.document_processor import DocumentProcessor


def scan_presentations(presentations_dir: str = "data/presentations") -> List[Dict]:
    """
    Scan presentations directory and collect file information.
    
    Args:
        presentations_dir: Path to presentations directory
        
    Returns:
        List of presentation metadata dictionaries
    """
    presentations = []
    presentations_path = Path(presentations_dir)
    
    if not presentations_path.exists():
        print(f"Directory {presentations_dir} does not exist. Creating it...")
        presentations_path.mkdir(parents=True, exist_ok=True)
        return presentations
    
    # Supported file extensions
    supported_extensions = {'.pdf', '.pptx', '.ppt'}
    
    for file_path in presentations_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            file_stat = file_path.stat()
            
            presentation_info = {
                "id": file_path.stem,
                "title": file_path.stem.replace('_', ' ').title(),
                "file_path": str(file_path.relative_to(Path.cwd())),
                "format": file_path.suffix.lower().lstrip('.'),
                "topic": "General",  # Can be extracted or set manually
                "key_concepts": [],
                "file_size": file_stat.st_size,
                "slide_count": 0,  # Will be updated after processing
                "processed": False,
                "created_at": datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                "modified_at": datetime.fromtimestamp(file_stat.st_mtime).isoformat()
            }
            presentations.append(presentation_info)
    
    return presentations


def generate_metadata(output_path: str = "data/metadata/presentations_metadata.json"):
    """
    Generate metadata file for all presentations.
    
    Args:
        output_path: Path to save metadata JSON file
    """
    print("Scanning presentations directory...")
    presentations = scan_presentations()
    
    metadata = {
        "presentations": presentations,
        "total_count": len(presentations),
        "last_updated": datetime.now().isoformat(),
        "version": "1.0"
    }
    
    # Ensure output directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save metadata
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Generated metadata for {len(presentations)} presentations")
    print(f"✓ Saved to {output_path}")
    
    return metadata


def validate_data_structure():
    """Validate that data directory structure is correct."""
    required_dirs = [
        "data/presentations",
        "data/metadata",
        "data/processed/chunks",
        "data/processed/embeddings"
    ]
    
    print("Validating data directory structure...")
    all_exist = True
    
    for dir_path in required_dirs:
        path = Path(dir_path)
        if not path.exists():
            print(f"✗ Missing: {dir_path}")
            path.mkdir(parents=True, exist_ok=True)
            print(f"  → Created: {dir_path}")
            all_exist = False
        else:
            print(f"✓ Found: {dir_path}")
    
    if all_exist:
        print("\n✓ All required directories exist")
    else:
        print("\n✓ Created missing directories")
    
    return all_exist


if __name__ == "__main__":
    print("=" * 50)
    print("Presentation Metadata Generator")
    print("=" * 50)
    
    # Validate structure
    validate_data_structure()
    print()
    
    # Generate metadata
    metadata = generate_metadata()
    
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  Total presentations: {metadata['total_count']}")
    print(f"  Last updated: {metadata['last_updated']}")
    print("=" * 50)

