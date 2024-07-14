import os
import cv2
import matplotlib.pyplot as plt
import yolov5


class HouseDetector:

    def load_model(self):
        # Initialize the YOLOv5 model (using the small version 'yolov5s' pre-trained on COCO dataset)
        os.makedirs(os.path.join('..', 'models'), exist_ok=True)
        model_filepath = os.path.join('..', 'models', 'yolov5s.pt')
        model = yolov5.load(model_filepath)
        return model

    def detect_houses(self, model, image_path):
        # set model parameters
        model.conf = 0.25  # NMS confidence threshold
        model.iou = 0.45  # NMS IoU threshold
        model.agnostic = False  # NMS class-agnostic
        model.multi_label = False  # NMS multiple labels per box
        model.max_det = 1000  # maximum number of detections per image

        # Load the image
        satellite_image = cv2.imread(image_path)
        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(satellite_image, cv2.COLOR_BGR2RGB)

        # perform inference
        results = model(image_rgb)

        # Extract bounding boxes and labels
        boxes = results.xyxy[0].cpu().numpy()  # Bounding boxes (xmin, ymin, xmax, ymax, confidence, class_id)
        labels = results.names  # Class labels

        # Draw bounding boxes on the image
        for box in boxes:
            xmin, ymin, xmax, ymax, confidence, cls_id = box
            # if labels[int(cls_id)] == 'house':  # Assuming the class name for houses is 'house' #TODO put back?
            cv2.rectangle(satellite_image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            cv2.putText(satellite_image, f'{labels[int(cls_id)]} {confidence:.2f}', (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return satellite_image

