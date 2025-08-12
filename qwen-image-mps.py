# /// script
# dependencies = [
#   "torch",
#   "diffusers @ git+https://github.com/huggingface/diffusers",
#   "transformers",
#   "accelerate",
#   "safetensors",
#   "huggingface-hub",
# ]
# ///

"""
This script wrapper allows direct execution via:
uv run qwen-image-mps.py

For package installation, use: pip install qwen-image-mps
"""

import sys
import os

# Add the src directory to Python path so we can import the local cli module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

if __name__ == "__main__":
    # Import cli.py from local source
    from qwen_image_mps import cli
    
    # Run the main function
    cli.main()
