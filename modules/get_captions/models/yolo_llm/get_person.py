from ultralytics import YOLO
import os

def get(image):

    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../output/yolov9c.pt"))

    model = YOLO(model_path)

    model.predict(image, conf=0.7, classes=0, save_crop=True)