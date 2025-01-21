import streamlit as st
import os
from langchain_cohere import ChatCohere
from PyPDF2 import PdfReader
import docx

# Predefined API key
os.environ["COHERE_API_KEY"] = "S7d32bATImsWVw2Hp2YvutpAGLBJFFWn57tFzBiS"

# Variable to store document content
document_content = ""

# Function to handle document upload for various formats (PDF, DOCX, TXT)
def upload_document(uploaded_file):
    global document_content
    file_extension = uploaded_file.name.split('.')[-1].lower()
    
    try:
        if file_extension == "txt":
            document_content = uploaded_file.getvalue().decode("utf-8")
        
        elif file_extension == "pdf":
            reader = PdfReader(uploaded_file)
            document_content = ""
            for page in reader.pages:
                document_content += page.extract_text()
        
        elif file_extension == "docx":
            doc = docx.Document(uploaded_file)
            document_content = ""
            for para in doc.paragraphs:
                document_content += para.text
        
        else:
            st.error("Unsupported file format. Please upload a .txt, .pdf, or .docx file.")
            return False
        
        st.success("Document uploaded successfully. You can now ask questions.")
        return True

    except Exception as e:
        st.error(f"Error reading the file: {e}")
        return False

# Function to handle role selection and message input
def get_response(role, user_message):
    if not document_content:
        st.warning("Please upload a document first.")
        return
    
    # Define the experience based on the role
    if role == "Sales Executive":
        experience = "3 years of experience as a Sales Executive."
    elif role == "Developer":
        experience = "3 years of experience as a Developer."
    
    # Initialize model
    model = ChatCohere(model="command-r-plus")
    
    # Send user message with role, experience, and document context
    response = model.invoke(f"Role: {role}, Experience: {experience}, Document content: {document_content}, Message: {user_message}")
    
    # Display the response
    st.text_area("Response", value=response, height=200)

# Streamlit UI
st.title("AI Chat Agent with Document Loader")

# File uploader for document
uploaded_file = st.file_uploader("Upload a document (txt, pdf, docx)", type=["txt", "pdf", "docx"])
if uploaded_file:
    upload_success = upload_document(uploaded_file)

# Role selection
role = st.selectbox("Select Role", ["Sales Executive", "Developer"])

# User message input
user_message = st.text_input("Enter your message:")

# Submit button to get AI response
if st.button("Submit") and uploaded_file:
    get_response(role, user_message)

