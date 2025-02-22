import cv2
import numpy as np
from typing import Optional, Tuple
from PIL import Image
from .config import FaceDetectionConfig, ProcessingResult
from .detector import FaceDetector

class ImageProcessor:
    """Image processing class for face detection and cropping"""
    
    def __init__(self, detector: FaceDetector):
        """Initialize with a face detector"""
        self.detector = detector
        self.config = detector.config

    def _crop_face(self, image: np.ndarray, box: np.ndarray) -> np.ndarray:
        """Crop face from image with margin"""
        h, w = image.shape[:2]
        x1, y1, x2, y2 = box
        
        width = x2 - x1
        height = y2 - y1
        margin = self.config.margin
        
        x1 = max(0, x1 - width * margin)
        x2 = min(w, x2 + width * margin)
        y1 = max(0, y1 - height * margin)
        y2 = min(h, y2 + height * margin)
        
        return image[int(y1):int(y2), int(x1):int(x2)]

    def process_image(self, image_path: str) -> ProcessingResult:
        """
        Process a single image
        
        Args:
            image_path: Path to input image
            
        Returns:
            ProcessingResult object containing the result and processed image
        """
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                return ProcessingResult(
                    success=False,
                    error_message="Failed to read image"
                )
            
            # Detect face
            box = self.detector.detect(image)
            if box is None:
                return ProcessingResult(
                    success=True,
                    face_detected=False,
                    error_message="No face detected"
                )
            
            # Crop and resize face
            face_img = self._crop_face(image, box)
            face_img = cv2.resize(face_img, self.config.target_size)
            
            # Convert to RGB for PIL
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(face_img)
            
            return ProcessingResult(
                success=True,
                face_detected=True,
                processed_image=pil_image,
                confidence=1.0  # TODO: Add actual confidence score
            )
            
        except Exception as e:
            return ProcessingResult(
                success=False,
                error_message=str(e)
            )

    def process_batch(self, image_paths: list, progress_callback=None) -> list:
        """
        Process multiple images
        
        Args:
            image_paths: List of image paths
            progress_callback: Optional callback function for progress updates
            
        Returns:
            List of ProcessingResult objects
        """
        results = []
        total = len(image_paths)
        
        for idx, path in enumerate(image_paths):
            result = self.process_image(path)
            results.append(result)
            
            if progress_callback:
                progress_callback(idx + 1, total)
                
        return results