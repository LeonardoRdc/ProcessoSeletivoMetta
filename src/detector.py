from ultralytics import YOLO
import numpy as np

class PersonDetector:


    def __init__(self, model_path="yolov8n.pt"):
    
        self.model = YOLO(model_path)

    def detect(self, frame):
       
        results = self.model.predict(frame, verbose=False)[0]

        detections = []

        for box in results.boxes:
            class_id = int(box.cls.item())
            confidence = float(box.conf.item())
            x1, y1, x2, y2 = box.xyxy[0].tolist()

          
            if class_id == 0:
                detections.append({
                    'bbox': (x1, y1, x2, y2),
                    'confidence': confidence,
                    'class_id': class_id
                })

        return detections
