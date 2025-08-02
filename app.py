import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

# Load your trained model
model = YOLO("best.pt")

st.title("Space Station Object Detection 🚀")
st.write("Detect Toolbox, Oxygen Tank, and Fire Extinguisher")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to OpenCV format
    img_array = np.array(image)
    results = model.predict(source=img_array)
    
    # Draw results on image
    annotated_frame = results[0].plot()
    st.image(annotated_frame, caption="Detection Result", use_column_width=True)
