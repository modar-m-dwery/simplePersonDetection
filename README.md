# YOLOv5 Person Detection

This project uses YOLOv5 to detect persons in images. The detected persons are highlighted with bounding boxes and confidence scores.

## Project Structure

```
yolov5_person_detection/
│
├── images/
│   ├── input.jpg
│   └── output.jpg
│
├── src/
│   ├── detect.py
│   ├── utils.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── run.py
```

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/yolov5_person_detection.git
    cd yolov5_person_detection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your input image in the `images/` directory and name it `input.jpg`.

2. Run the detection script:
    ```sh
    python run.py
    ```

3. The output image with bounding boxes will be saved as `output.jpg` in the `images/` directory.

## Code Explanation

### `detect.py`

- `load_model()`: Loads the pre-trained YOLOv5 model.
- `detect_and_draw(input_img_path, output_img_path)`: Detects persons in the input image and draws bounding boxes around them.

### `utils.py`

- `filter_persons(results)`: Filters out non-person detections.
- `draw_bounding_boxes(img, persons)`: Draws bounding boxes around detected persons.

## Example

### Input Image

![Input Image](images/input.jpg)

### Output Image

![Output Image](images/output.jpg)
```