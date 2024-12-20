# Image Size Filter Script

This Python script automates the image selection process by filtering images based on their dimensions. It automatically copies images that meet minimum size requirements to a separate folder, making it particularly useful for preparing datasets for LoRA model training.

## Problem Solved

When collecting images for LoRA model training, you often download entire galleries containing files of various sizes. This script automatically filters images that meet the minimum requirements (512x512 pixels), eliminating the need for manual verification.

## Features

- Automatically analyzes all images in the current working directory
- Verifies that both dimensions (width and height) are >= 512 pixels
- Automatically creates an "ok" subfolder for valid images
- Copies (doesn't move) qualifying images to the "ok" folder
- Keeps the original folder intact
- Provides real-time feedback on operations
- Processes files in parallel for improved performance

## Requirements

- Python 3.x
- Pillow (PIL) library
- Operating System: Windows/Linux/MacOS

## Installation

1. Ensure Python is installed
2. Install the Pillow library if not present:
```bash
pip install Pillow
```

## Usage

1. Place the script in the folder containing the images you want to filter
2. Run the script:
```bash
python image-filter.py
```

The script will automatically:
- Create an "ok" subfolder in the current directory
- Copy all images meeting the size requirements into it
- Process files in parallel for faster execution

## Output

During execution, the script will display:
- Name and dimensions of each copied image
- Any errors encountered during the process
- Completion message when finished

## Notes

- The script doesn't modify or delete original files
- Images are copied, not moved, preserving the original archive
- Files with the same name in the destination folder will be overwritten
- The script uses parallel processing to improve performance

## Tips

- Before proceeding with dataset captioning, it's recommended to verify the contents of the "ok" folder
- The script automatically uses the current working directory, so no path configuration is needed
- The minimum required size (512x512) is hardcoded in the script - modify the value in the code if you need different dimensions
