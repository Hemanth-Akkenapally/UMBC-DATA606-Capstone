import streamlit as st # type: ignore
import subprocess
import os

def run_darknet_detection(image_path):
    darknet_command = f"./darknet detector test /content/OIDv4_ToolKit/darknet/cfg/coco.data " \
                      f"/content/OIDv4_ToolKit/darknet/cfg/yolov4-custom.cfg " \
                      f"/content/OIDv4_ToolKit/darknet/cfg/custom.weights {image_path}"
    try:
        result = subprocess.run(darknet_command.split(), capture_output=True, text=True, timeout=120)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return None, "Darknet detection process timed out."

def main():
    st.title("Darknet Object Detection")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_image_path = "uploaded_image.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Run Object Detection"):
            stdout, stderr = run_darknet_detection(temp_image_path)
            if stderr:
                st.error(f"Error: {stderr}")
            else:
                st.success("Object detection completed successfully!")
                st.text(stdout)

            # Display the output image if it exists
            output_image_path = "/content/OIDv4_ToolKit/darknet/predictions.jpg"
            if os.path.exists(output_image_path):
                st.image(output_image_path, caption="Detected Objects", use_column_width=True)

if __name__ == "__main__":
    main()
