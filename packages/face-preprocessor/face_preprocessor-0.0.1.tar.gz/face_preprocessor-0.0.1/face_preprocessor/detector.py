import torch
import numpy as np
from typing import Optional, Tuple
from retinaface.pre_trained_models import get_model
from torchvision.ops import nms
from .config import FaceDetectionConfig

class FaceDetector:
    """Face detection using RetinaFace"""
    
    def __init__(self, config: FaceDetectionConfig):
        """Initialize the face detector with given configuration"""
        self.config = config
        self.model = get_model(config.model_name, max_size=config.max_size)
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def detect(self, image: np.ndarray) -> Optional[np.ndarray]:
        """
        Detect faces in image and return the largest face bounding box
        
        Args:
            image: Input image as numpy array (BGR format)
            
        Returns:
            Bounding box as [x1, y1, x2, y2] or None if no face detected
        """
        with torch.no_grad():
            faces = self.model.predict_jsons(image)
            
            if not faces:
                return None
            
            # Extract boxes and scores
            boxes = []
            scores = []
            for face in faces:
                if face['score'] < self.config.min_confidence:
                    continue
                box = face['bbox']
                boxes.append([box[0], box[1], box[2], box[3]])
                scores.append(face['score'])
            
            if not boxes:
                return None
                
            # Convert to tensors for NMS
            boxes = torch.tensor(boxes, dtype=torch.float32).to(self.device)
            scores = torch.tensor(scores, dtype=torch.float32).to(self.device)
            
            # Apply NMS
            keep = nms(boxes, scores, iou_threshold=0.5)
            
            if len(keep) == 0:
                return None
                
            # Convert back to numpy
            boxes = boxes[keep].cpu().numpy()
            
            # Get the largest face
            areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
            largest_face_idx = np.argmax(areas)
            
            return boxes[largest_face_idx]