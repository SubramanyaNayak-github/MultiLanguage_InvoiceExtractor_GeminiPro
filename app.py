from dotenv import load_dotenv

load_dotenv() ## Load the env variables from .env



import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


from PIL import Image
import textwrap
import PyPDF2
import pathlib



## To get model response from gemini model


def get_model_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision') 
    response = model.generate_content([input,image[0],prompt])
    return response.text


## for Input Image setup


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [ {
            'mime_type': uploaded_file.type,
            'data' : bytes_data
        }]
        return image_parts
    


## Initialize Streamlit application
    
st.set_page_config(page_title = 'MultiLanguage Invoice Exctracor')

st.header('Gemini Vision MultiLanguage Invoice Exctracor Application')

upload_image = st.file_uploader('uploade your image here', type=['jpg','jpeg','png'])
image = ''
input_text = st.text_input('Input prompt', key ='input')

if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image,caption ='Uploaded image',use_column_width=True)



submit = st.button('Click here for more information')


input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image 
                
               """



## If ask button is clicked

if submit:
    image_data = input_image_setup(upload_image)
    response=get_model_response(input_prompt,image_data,input_text)
    st.subheader("The Response is")
    st.write(response)