import streamlit as st
import os
import subprocess
import requests

def run_darknet(image_path):
    # Here you would handle the call to your remote Colab or local environment
    # For example, using subprocess to call darknet directly if it's local:
    # Make sure to adjust paths to your darknet configuration and weights
    result = subprocess.run([
        './darknet', 
        'detector', 'test',
        '/content/OIDv4_ToolKit/darknet/cfg/coco.data',
        '/content/OIDv4_ToolKit/darknet/cfg/yolov4-custom.cfg',
        '/content/OIDv4_ToolKit/darknet/cfg/custom.weights',
        '/content/OIDv4_ToolKit/darknet/car2.jpg'
    ], capture_output=True, text=True)
    return result.stdout

def download_image(image_url):
    # Function to download image from URL provided by Colab after processing
    r = requests.get(image_url)
    with open('predictions.jpg', 'wb') as f:
        f.write(r.content)

def load_image(image_file):
    # Assuming the image is saved locally after processing
    return 'predictions.jpg'

st.title("YOLO License Plate Detection")
st.write("Upload an image of the car to detect the license plate.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File Uploaded Successfully.")

    if st.button('Run Detection'):
        image_path = os.path.join("tempDir", uploaded_file.name)
        result = run_darknet(image_path)
        st.text(result)

        # Optionally download and show the image
        # You need to replace 'your_colab_image_url' with the actual URL of the image
        # download_image('your_colab_image_url')
        # predictions_path = load_image('predictions.jpg')
        # st.image(predictions_path, caption='Predicted Image', use_column_width=True)
