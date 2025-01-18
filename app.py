from dotenv import load_dotenv
import streamlit as st
from PIL import Image          #get image info#
import google.generativeai as genai
import os
from src.helper import *


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

load_dotenv()


    


st.set_page_config(page_title="Gemini Invoice Reader")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   

if uploaded_file is not None:
 
    image = Image.open(uploaded_file)
    
    # Display the image
    max_width = 400 
    aspect_ratio = image.size[1] / image.size[0]  # height/width
    new_width = max_width
    new_height = int(max_width * aspect_ratio)
    
    # Resize image
    resized_image = image.resize((new_width, new_height))
    
    # Display the resized image
    st.image(resized_image, 
             caption="Uploaded Image.", 
             use_container_width=False,
             width=max_width)

submit = st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_vision_response(input_prompt, image_data, input)
    st.subheader("OUTPUT:")
    st.write(response)