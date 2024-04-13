import streamlit as st
import subprocess
import cv2
import numpy as np
from PIL import Image

# Function to parse YOLOv4 output and extract bounding box coordinates
def parse_yolov4_output(output):
    # Simplified parsing function for YOLOv4 output
    detections = []
    for line in output.split('\n'):
        if line.startswith('Bounding Box'):
            parts = line.split(':')
            coordinates = parts[1].strip().split(',')
            detections.append(tuple(map(int, coordinates)))
    return detections

# Function to perform license plate detection using YOLOv4
def detect_license_plate(image_path, weights_path, cfg_path, data_path):
    # Run YOLOv4 command to detect license plates
    command = ["./darknet", "detector", "test", data_path, cfg_path, weights_path, image_path]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    # Parse YOLOv4 output to extract license plate detections
    detections = parse_yolov4_output(output)

    # Draw rectangles around detected license plates
    image = cv2.imread(image_path)
    for (x, y, w, h) in detections:
        cv2.rectangle(image, (x, y), (w, h), (255, 0, 0), 2)

    return image

def main():
    st.title('Automatic Number Plate Recognition (ANPR)')

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button('Detect License Plate'):
            weights_path = "/content/OIDv4_ToolKit/darknet/cfg/custom.weights"
            cfg_path = "/content/OIDv4_ToolKit/darknet/cfg/yolov4-custom.cfg"
            data_path = "/content/OIDv4_ToolKit/darknet/cfg/coco.data"

            with st.spinner('Detecting...'):
                detected_image = detect_license_plate(uploaded_image.name, weights_path, cfg_path, data_path)
                st.image(detected_image, caption="License Plate Detected", use_column_width=True)

if __name__ == "__main__":
    main()
