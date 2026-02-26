from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame)
        return results

    def extract_objects(self, results, frame_shape, confidence_threshold=0.6):
        boxes = results[0].boxes
        names = results[0].names

        frame_area = frame_shape[0] * frame_shape[1]
        detected_objects = []

        for box in boxes:
            confidence = float(box.conf[0])
            cls_id = int(box.cls[0])

            if confidence > confidence_threshold:
                object_name = names[cls_id]

                x1, y1, x2, y2 = box.xyxy[0]
                box_area = (x2 - x1) * (y2 - y1)

                area_ratio = box_area / frame_area

                # Distance estimation
                if area_ratio > 0.20:
                    distance = "very close"
                elif area_ratio > 0.08:
                    distance = "near"
                elif area_ratio > 0.03:
                    distance = "at a medium distance"
                else:
                    distance = "far away"

                detected_objects.append((object_name, distance))

        return detected_objects