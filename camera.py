import streamlit as st
from PIL import Image

st.subheader("Color to Gray scale convertor")

uploaded_image =  st.file_uploader("Upload_img")

with st.expander("start camera"):
    camera_image = st.camera_input("camera")

if camera_image:
    print(camera_image)
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_upload_img = img.convert("L")
    st.image(gray_upload_img)
