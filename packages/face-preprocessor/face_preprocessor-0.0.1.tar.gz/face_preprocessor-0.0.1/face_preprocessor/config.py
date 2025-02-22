from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class FaceDetectionConfig:
    """Configuration for face detection parameters"""
    model_name: str
    max_size: int
    min_confidence: float = 0.9
    target_size: Tuple[int, int] = (224, 224)
    margin: float = 0.2

@dataclass
class ProcessingResult:
    """Result of image processing"""
    success: bool
    processed_image: Optional[object] = None
    error_message: str = ""
    face_detected: bool = False
    confidence: float = 0.0