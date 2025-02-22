# Face Preprocessor

A Python package for face detection and preprocessing in images. This package provides tools for detecting faces, cropping them with margins, and preparing them for further processing or machine learning tasks.

## Features

- Face detection using RetinaFace
- Face cropping with customizable margins
- Batch processing capabilities
- Support for various input formats
- Configurable preprocessing parameters
- Azure Blob Storage support (optional)

## Installation

```bash
pip install face-preprocessor
```

## Quick Start

```python
from face_preprocessor import FaceDetector, ImageProcessor
from face_preprocessor.config import FaceDetectionConfig

# Initialize configuration
config = FaceDetectionConfig(
    model_name="resnet50",
    max_size=1024,
    min_confidence=0.9
)

# Create detector and processor
detector = FaceDetector(config)
processor = ImageProcessor(detector)

# Process a single image
result = processor.process_image("path/to/image.jpg")
if result.success:
    result.processed_image.save("output.jpg")

