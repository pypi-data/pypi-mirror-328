# PDF Image Extractor

A tool to extract high-quality images from PDF files while preserving metadata and positioning information.

## Features

- Extracts images in their original quality without recompression
- Preserves image metadata including DPI and positioning
- Detects and skips duplicate images
- Generates detailed JSON metadata file
- Sorts images by their position on the page

## Installation

```bash
pip install pdfimageextractor
```

## Usage

```bash
pdfextractimages <PDF_FILE> [OUTPUT_FOLDER]
```

Arguments:
- `PDF_FILE`: Path to the PDF file to process
- `OUTPUT_FOLDER`: Optional directory to save extracted images (defaults to PDF_FILE_images)

## Output

The tool creates:
- Original quality images extracted from the PDF
- A `image_metadata.json` file containing detailed information about each image
