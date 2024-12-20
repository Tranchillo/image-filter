
# Image Size Filter Script

This Python script was developed to automate the process of selecting images during the preparation of datasets for training LoRA models. It automatically filters images based on their dimensions, copying only those that meet the minimum requirements into a separate folder.

## Problem Solved

When collecting images for training LoRA models, entire galleries of images with various sizes are often downloaded. Manually checking and selecting images that meet the minimum requirements (512x512 pixels) can be time-consuming. This script fully automates this process.

## Features

- Analyzes all images in the specified folder
- Verifies that both dimensions (width and height) are >= 512 pixels
- Automatically creates an "ok" subfolder for valid images
- Copies (does not move) images that meet the requirements into the "ok" folder
- Keeps the original folder intact
- Provides real-time feedback on performed operations

## Requirements

- Python 3.x
- Pillow (PIL) library
- Operating system: Windows/Linux/MacOS

## Installation

1. Make sure Python is installed
2. Install the Pillow library if not already installed:
```bash
pip install Pillow
```

## Usage

1. Place the script in the folder containing the images to filter
2. Modify the path in the `source_dir` variable with your folder path:
```python
source_dir = r"C:\image-filter"  # Modify this path
```
3. Run the script:
```bash
python image_filter.py
```

The script will automatically create an "ok" subfolder and copy all images meeting the size requirements into it.

## Output

During execution, the script will display:
- Name and dimensions of each copied image
- Any errors encountered during the process
- Completion message

## Notes

- The script does not modify or delete the original files
- Images are copied, not moved, allowing the original archive to remain intact
- Files with the same name in the destination folder will be overwritten

## Tips

- Before proceeding with dataset captioning, it is recommended to check the contents of the "ok" folder
- To change the minimum required size, modify the value `512` in the size check
