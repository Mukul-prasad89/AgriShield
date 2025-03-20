import streamlit as st
from PIL import Image
import numpy as np
import time


def dummy_diagnose(image):
    """Simulates a disease diagnosis process."""
    time.sleep(2)  
    diseases = ["Healthy", "Blight", "Rust", "Mosaic Virus", "Leaf Spot"]
    prediction = np.random.choice(diseases) 
    return prediction


st.set_page_config(page_title="AGRI-SHIELD", page_icon="🌿", layout="wide")


st.sidebar.title("🌿 AGRI-SHIELD")

page = st.sidebar.radio("Navigate", ["Home", "Services", "About", "Contact"])


if page == "Home":
    st.title("🌿 AGRI-SHIELD")
    st.write("**Welcome to AgriShield**, a trusted companion in protecting and enhancing crop health!"
    "Harness the power of technology to detect diseases early, get expert recommendations, and ensure a thriving harvest."
    " Let’s grow smarter, together")

    
    
    col1, col2 = st.columns([1, 2])  

    with col1:
       

        with st.container():
            uploaded_file = st.file_uploader("**Choose a leaf image...**", type=["jpg", "jpeg", "png"])
        
        with st.container():
            camera_file = st.camera_input("**Take a picture**")

    
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    elif camera_file is not None:
        image = Image.open(camera_file)
        st.image(image, caption="Captured Image", use_column_width=True)

    if image:
        st.write("Analyzing...")

        
        prediction = dummy_diagnose(image)
        st.success(f"Diagnosis: {prediction}")

        
        st.markdown("###Additional Information")
        st.write("Here are some details about crop diseases and possible treatments.")

        if prediction != "Healthy":
            st.warning(f"Detected disease: {prediction}. Consider applying appropriate treatments.")
        else:
            st.success("Your plant looks healthy! Keep maintaining good agricultural practices.")


elif page == "Services":
    st.title("Our Services")
    st.write("""
    - **Crop Disease Detection**: Upload or capture images of your crops to detect diseases.
    - **Disease Analysis**: Get insights and statistics on detected crop diseases.
    - **Treatment Suggestions**: Receive expert recommendations for managing plant diseases.
    - **Nearby Agricultural Centers**: Locate nearby agricultural help centers and experts.
    """)


elif page == "About":
    st.title("About AGRI-SHIELD")
    st.write("""
    **AGRI-SHIELD** is an AI-powered platform that helps farmers detect plant diseases using image processing.
    
    -Powered by **Machine Learning & AI**.
    -Designed for **Farmers & Agricultural Experts**.
    -Provides **Instant Diagnosis & Treatment Suggestions**.
    """)


elif page == "Contact":
    st.title("📞 Contact Us")
    st.write("""
    Email: **agrishieldd@gmail.com**
    Location: **New Delhi, India**
    Phone: **+91 7005079922**
    """)
