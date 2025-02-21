import os
import pytest
from pdfimageextractor.extractpdfimages import extract_high_quality_images_from_pdf

def test_extract_images_from_nonexistent_file():
    """Test that appropriate error is raised for non-existent file"""
    with pytest.raises(FileNotFoundError):
        extract_high_quality_images_from_pdf("nonexistent.pdf", "output")

def test_extract_images_invalid_output():
    """Test handling of invalid output directory"""
    # Create a file where the output directory should be
    with open("blocked_dir", "w") as f:
        f.write("blocking file")
    
    with pytest.raises(NotADirectoryError):
        extract_high_quality_images_from_pdf("test.pdf", "blocked_dir")
    
    os.remove("blocked_dir")
