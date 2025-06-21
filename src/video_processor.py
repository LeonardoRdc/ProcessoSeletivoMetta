import os
import cv2
import json
from datetime import datetime

class VideoProcessor:
  

    def __init__(self, input_video_path, output_dir, alert_threshold, detector):
      
        self.input_video_path = input_video_path
        self.output_dir = output_dir
        self.alert_threshold = alert_threshold
        self.detector = detector

        
        self.output_video_path = os.path.join(self.output_dir, "output_video.mp4")
        self.history_json_path = os.path.join(self.output_dir, "history.json")
        self.alerts_json_path = os.path.join(self.output_dir, "alerts.json")

       
        os.makedirs(self.output_dir, exist_ok=True)

    def process_video(self):
       
        cap = cv2.VideoCapture(self.input_video_path)

        if not cap.isOpened():
            raise FileNotFoundError(f"Não foi possível abrir o vídeo: {self.input_video_path}")

        # Configurar saída de vídeo
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = cv2.VideoWriter(self.output_video_path, fourcc, fps, (frame_width, frame_height))

        history_data = []
        alerts_data = []

        frame_id = 0
        alert_id = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

           
            detections = self.detector.detect(frame)

           
            person_count = len(detections)

           
            history_data.append({
                "id": frame_id,
                "count": person_count
            })

           
            if person_count >= self.alert_threshold:
                alerts_data.append({
                    "id": frame_id,
                    "count": person_count
                })

           
            for det in detections:
                x1, y1, x2, y2 = map(int, det['bbox'])
                confidence = det['confidence']

              
                cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

            out.write(frame)

            frame_id += 1

       
        self._save_json(self.history_json_path, history_data)
        self._save_json(self.alerts_json_path, alerts_data)

       
        cap.release()
        out.release()

        print(f"Processamento concluído. Saídas salvas em: {self.output_dir}")

    def _save_json(self, path, data):
    
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
