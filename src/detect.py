import torch
from PIL import Image, ImageDraw
from pathlib import Path
from src.utils import draw_bounding_boxes, filter_persons

def load_model():
    return torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

def detect_and_draw(input_img_path, output_img_path):
    model = load_model()
    img = Image.open(input_img_path)
    results = model(img)
    persons = filter_persons(results)
    draw_img = draw_bounding_boxes(img, persons)
    draw_img.save(output_img_path)
    print(f"Image with bounding boxes saved at: {output_img_path}")

if __name__ == "__main__":
    input_img_path = "images/input.jpg"
    output_img_path = "images/output.jpg"
    detect_and_draw(input_img_path, output_img_path)
