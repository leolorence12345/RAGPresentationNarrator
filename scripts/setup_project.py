"""
Setup script to initialize the project structure.
Run this script to create all necessary directories and files.
"""

from pathlib import Path
import json
from datetime import datetime


def create_directory_structure():
    """Create all necessary directories."""
    directories = [
        "data/presentations",
        "data/processed/chunks",
        "data/processed/embeddings",
        "data/metadata",
        "models",
        "cache/responses",
        "docs",
        "examples",
        "scripts"
    ]
    
    print("Creating directory structure...")
    for directory in directories:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")
    
    print("\n✓ Directory structure created")


def create_initial_metadata():
    """Create initial metadata file."""
    metadata_path = Path("data/metadata/presentations_metadata.json")
    
    if metadata_path.exists():
        print(f"  ⚠ Metadata file already exists: {metadata_path}")
        return
    
    metadata = {
        "presentations": [],
        "total_count": 0,
        "last_updated": datetime.now().isoformat(),
        "version": "1.0"
    }
    
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"  ✓ Created initial metadata file: {metadata_path}")


def create_config_from_example():
    """Create config.yaml from example if it doesn't exist."""
    config_path = Path("config.yaml")
    example_path = Path("config.yaml.example")
    
    if config_path.exists():
        print(f"  ⚠ Config file already exists: {config_path}")
        return
    
    if example_path.exists():
        import shutil
        shutil.copy(example_path, config_path)
        print(f"  ✓ Created config.yaml from example")
        print(f"  ⚠ Please edit config.yaml with your API keys!")
    else:
        print(f"  ✗ Example config not found: {example_path}")


def verify_structure():
    """Verify that the structure is correct."""
    print("\nVerifying project structure...")
    
    required_dirs = [
        "data/presentations",
        "data/metadata",
        "models",
        "cache/responses",
        "src/pipeline",
        "src/agents",
        "src/cache",
        "src/utils",
        "src/prompts"
    ]
    
    all_exist = True
    for directory in required_dirs:
        path = Path(directory)
        if path.exists():
            print(f"  ✓ {directory}")
        else:
            print(f"  ✗ Missing: {directory}")
            all_exist = False
    
    return all_exist


if __name__ == "__main__":
    print("=" * 60)
    print("RAG Presentation Narrator - Project Setup")
    print("=" * 60)
    print()
    
    # Create directories
    create_directory_structure()
    print()
    
    # Create initial files
    print("Creating initial files...")
    create_initial_metadata()
    create_config_from_example()
    print()
    
    # Verify structure
    if verify_structure():
        print("\n✓ Project structure is ready!")
        print("\nNext steps:")
        print("  1. Edit config.yaml with your API keys")
        print("  2. Add presentation files to data/presentations/")
        print("  3. Run: python data/process_presentations.py")
    else:
        print("\n⚠ Some directories are missing. Please check the structure.")
    
    print("=" * 60)

