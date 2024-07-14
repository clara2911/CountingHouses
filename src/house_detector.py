import os
import cv2
import matplotlib.pyplot as plt
import yolov5

def load_model():
    # Initialize the YOLOv5 model (using the small version 'yolov5s' pre-trained on COCO dataset)
    os.makedirs(os.path.join('..', 'models'), exist_ok=True)
    model_filepath = os.path.join('..', 'models', 'yolov5s.pt')
    model = yolov5.load(model_filepath)
    return model

def detect_houses(model, image_path):
    # # set model parameters
    # model.conf = 0.25  # NMS confidence threshold
    # model.iou = 0.45  # NMS IoU threshold
    # model.agnostic = False  # NMS class-agnostic
    # model.multi_label = False  # NMS multiple labels per box
    # model.max_det = 1000  # maximum number of detections per image
    #
    # # set image
    # img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'
    #
    # # perform inference
    # results = model(img)

    #
    # Load the image
    image = cv2.imread(image_path)
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # perform inference
    results = model(image_rgb)

    # Extract bounding boxes and labels
    boxes = results.xyxy[0].cpu().numpy()  # Bounding boxes (xmin, ymin, xmax, ymax, confidence, class_id)
    labels = results.names  # Class labels

    # Draw bounding boxes on the image
    for box in boxes:
        xmin, ymin, xmax, ymax, confidence, cls_id = box
        if labels[int(cls_id)] == 'house':  # Assuming the class name for houses is 'house'
            cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            cv2.putText(image, f'{labels[int(cls_id)]} {confidence:.2f}', (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save and display the result
    output_image_path = 'detected_houses.png'
    cv2.imwrite(output_image_path, image)
    print(f"Detected houses image saved as {output_image_path}")

    # Display the image with bounding boxes
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Example usage
image_path = '../images/satellite_image.png'  # Path to the saved satellite image
model = load_model()
detect_houses(model, image_path)
