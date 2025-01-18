import google.generativeai as genai

#Fucntion to load Gemini Pro vision model and get responses

def get_vision_response(input,image,prompt):

    #input is the message given to LLm which would decide the behaviour of the model#
    model=genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([input,image[0],prompt])
    return response.text


#Converting image to bytes for uploading it

def input_image_setup(uploaded_file):
    
    if uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")