"""
Utility script to validate presentation files.
Checks if files are readable and can be processed.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils.document_processor import DocumentProcessor


def validate_presentation_file(file_path: Path) -> tuple[bool, str]:
    """
    Validate a single presentation file.
    
    Args:
        file_path: Path to presentation file
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not file_path.exists():
        return False, "File does not exist"
    
    if not file_path.is_file():
        return False, "Path is not a file"
    
    # Check file extension
    supported_extensions = {'.pdf', '.pptx', '.ppt'}
    if file_path.suffix.lower() not in supported_extensions:
        return False, f"Unsupported file type: {file_path.suffix}"
    
    # Try to extract text
    try:
        if file_path.suffix.lower() == '.pdf':
            text = DocumentProcessor.extract_text_from_pdf(file_path)
        elif file_path.suffix.lower() in {'.pptx', '.ppt'}:
            text = DocumentProcessor.extract_text_from_pptx(file_path)
        else:
            return False, "Unknown file type"
        
        if not text or len(text.strip()) < 10:
            return False, "File appears to be empty or unreadable"
        
        return True, f"Valid ({len(text)} characters extracted)"
    
    except Exception as e:
        return False, f"Error processing file: {str(e)}"


def validate_all_presentations(presentations_dir: str = "data/presentations"):
    """
    Validate all presentations in the directory.
    
    Args:
        presentations_dir: Path to presentations directory
    """
    presentations_path = Path(presentations_dir)
    
    if not presentations_path.exists():
        print(f"✗ Directory {presentations_dir} does not exist")
        return
    
    print("=" * 60)
    print("Validating Presentations")
    print("=" * 60)
    
    files = list(presentations_path.glob("*"))
    presentation_files = [f for f in files if f.is_file() and f.suffix.lower() in {'.pdf', '.pptx', '.ppt'}]
    
    if not presentation_files:
        print(f"No presentation files found in {presentations_dir}")
        return
    
    print(f"\nFound {len(presentation_files)} presentation file(s)\n")
    
    valid_count = 0
    invalid_count = 0
    
    for file_path in presentation_files:
        is_valid, message = validate_presentation_file(file_path)
        status = "✓" if is_valid else "✗"
        print(f"{status} {file_path.name:40s} - {message}")
        
        if is_valid:
            valid_count += 1
        else:
            invalid_count += 1
    
    print("\n" + "=" * 60)
    print(f"Summary: {valid_count} valid, {invalid_count} invalid")
    print("=" * 60)


if __name__ == "__main__":
    validate_all_presentations()

