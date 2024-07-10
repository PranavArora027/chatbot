from openai import OpenAI
import streamlit as st
import boto3
from dotenv import load_dotenv
import os
from st_pages import hide_pages

hide_pages(['login'])

load_dotenv()
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# Create an S3 client
s3_client = boto3.client('s3')


st.title("ChatGPT-like clone")

client = OpenAI(api_key=os.getenv('API_KEY'))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


# Function to upload a file to S3
def upload_to_s3(file, bucket_name, object_name):
    try:
        s3_client.upload_fileobj(file, bucket_name, object_name)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error uploading file to S3: {str(e)}")

# Add a file uploader button
uploaded_file = st.file_uploader("Upload Files", type=["txt", "pdf", "png", "jpg"], key="my_file_uploader")

# If a file is uploaded
if uploaded_file is not None:
    # Specify the object name in the S3 bucket (you can modify this according to your needs)
    st.write("File uploaded successfully!")
    object_name = "uploaded_files/" + uploaded_file.name

    # Call the function to upload the file to S3
    upload_to_s3(uploaded_file, S3_BUCKET_NAME, object_name)