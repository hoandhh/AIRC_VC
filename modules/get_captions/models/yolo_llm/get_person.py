from ultralytics import YOLO

def get(image):
    model = YOLO('yolov9c.pt')

    model.predict(image, conf=0.7, classes=0, save_crop=True)