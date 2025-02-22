import cv2
import numpy as np
from typing import Tuple

def validate_image(image: np.ndarray) -> bool:
    """Validate image array"""
    if not isinstance(image, np.ndarray):
        return False
    if len(image.shape) != 3:
        return False
    if image.shape[2] != 3:
        return False
    return True

def resize_keep_aspect(image: np.ndarray, max_size: int) -> np.ndarray:
    """Resize image keeping aspect ratio"""
    h, w = image.shape[:2]
    if h > w:
        new_h = max_size
        new_w = int(w * max_size / h)
    else:
        new_w = max_size
        new_h = int(h * max_size / w)
    return cv2.resize(image, (new_w, new_h))