#
# # Import libraries
# from dotenv import load_dotenv
# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai
#
# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#
# if GOOGLE_API_KEY:
#     genai.configure(api_key=GOOGLE_API_KEY)
# else:
#     st.error("⚠️ Google API Key not found. Please set it in the environment variables.")
#
#
# # Function to get response from Gemini model
# def get_gemini_response(input_text, image_data):
#     try:
#         model = genai.GenerativeModel('gemini-1.0-pro-vision')  # Corrected Model Name
#         response = model.generate_content([input_text, image_data])
#         return response.text
#     except Exception as e:
#         return f"❌ Error: {str(e)}"
#
#
# # Function to process uploaded image
# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         return Image.open(uploaded_file)  # Open image with PIL
#     return None
#
#
# # Streamlit UI Design
# st.set_page_config(page_title="🧾 Invoice Q&A Chatbot", layout="wide")
#
# # Custom Styling (Red Theme)
# st.markdown("""
#     <style>
#         .title {text-align: center; font-size: 36px; font-weight: bold; color: #D72638;}
#         .subtitle {text-align: center; font-size: 20px; color: #333333;}
#         .footer {text-align: center; font-size: 16px; margin-top: 30px; color: #666666;}
#         .stButton>button {background-color: #D72638; color: white; font-size: 18px; border-radius: 8px; padding: 10px 20px;}
#         .stButton>button:hover {background-color: #A61C2A;}
#     </style>
# """, unsafe_allow_html=True)
#
# # Sidebar for Navigation
# with st.sidebar:
#     st.image(
#         "img.png",
#         width=250)
#
#     st.markdown("<h2 style='color: #D72638;'>🔍 Invoice Q&A Chatbot</h2>", unsafe_allow_html=True)
#     st.markdown("<p>🤖 Ask questions about invoices using AI-powered technology.</p>", unsafe_allow_html=True)
#     st.markdown("---")
#     st.markdown("<h3 style='color: #D72638;'>📌 Features</h3>", unsafe_allow_html=True)
#     st.markdown("""
#     ✅ AI-Powered Invoice Analysis
#     📸 Image-Based Q&A
#     💬 Instant Answers
#     ⚡ Fast & Reliable
#     🎨 Simple & Elegant UI
#     """)
#
# # Page Title
# st.markdown('<p class="title">📄 Invoice Q&A Chatbot</p>', unsafe_allow_html=True)
# st.markdown("""
#     <p style="
#         font-size: 18px;
#         font-weight: bold;
#         color: green;
#         text-align: center;
#         margin-top: 10px;">
#         📸 Upload an invoice image and ask a question about it.
#     </p>
# """, unsafe_allow_html=True)
#
# # User Input
# st.write("💡 **Enter your question:**")
# input_text = st.text_input("", key="input", placeholder="E.g. What is the total amount on this invoice?")
#
# # File Uploader for Image
# st.write("📸 **Upload an invoice image:**")
# uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
#
# # Display Uploaded Image
# image_data = None
# if uploaded_file:
#     image_data = input_image_setup(uploaded_file)
#     st.image(image_data, caption="🖼️ Uploaded Invoice", use_column_width=True)
#
# # Analyze Button
# st.markdown("<br>", unsafe_allow_html=True)  # Line break for spacing
# submit = st.button("🔍 Analyze Image")
#
# # Processing
# if submit:
#     if not uploaded_file:
#         st.error("⚠️ Please upload an invoice image first!")
#     elif not input_text.strip():
#         st.error("⚠️ Please enter a question!")
#     else:
#         st.success("✅ Processing your request... Please wait.")
#
#         input_prompt = """
#             You are an AI assistant specializing in invoice analysis.
#             You will receive an invoice image and a question.
#             Provide an accurate answer based on the invoice details.
#         """
#         response = get_gemini_response(input_prompt, image_data)
#
#         st.subheader("💡 AI Response:")
#         st.write(response)
#
# # Footer - "Made By"
# st.markdown('<p class="footer">🚀 Made with ❤️ by <b>Prarthana</b></p>', unsafe_allow_html=True)







# Import libraries
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("⚠️ Google API Key not found. Please set it in the environment variables.")


# Function to get response from Gemini model
def get_gemini_response(input_text, image_data):
    try:
        model = genai.GenerativeModel('gemini-1.0-pro-vision')  # Corrected Model Name
        response = model.generate_content([input_text, image_data])
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"


# Function to process uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return Image.open(uploaded_file)  # Open image with PIL
    return None


# Streamlit UI Design
st.set_page_config(page_title="🧾 Invoice Q&A Chatbot", layout="wide")

# Custom Styling (Red Theme)
st.markdown("""
    <style>
        .title {text-align: center; font-size: 38px; font-weight: bold; color: #D72638; margin-bottom: 10px;}
        .subtitle {text-align: center; font-size: 20px; color: black; margin-bottom: 20px;}
        .upload-text {font-size: 20px; font-weight: bold; color: green; text-align: center; margin-top: 15px;}
        .footer {text-align: center; font-size: 16px; margin-top: 30px; color: #666666;}
        .stButton>button {background-color: #D72638; color: white; font-size: 18px; border-radius: 8px; padding: 12px 25px;}
        .stButton>button:hover {background-color: #A61C2A;}
    </style>
""", unsafe_allow_html=True)

# Sidebar for Navigation
with st.sidebar:
    st.image("img.png", width=250)  # Replaced with a robot image

    st.markdown("<h2 style='color: #D72638;'>🔍 Invoice Q&A Chatbot</h2>", unsafe_allow_html=True)
    st.markdown("<p>🤖 Ask questions about invoices using AI-powered technology.</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='color: #D72638;'>📌 Features</h3>", unsafe_allow_html=True)
    st.markdown("""
    ✅ AI-Powered Invoice Analysis  
    📸 Image-Based Q&A  
    💬 Instant Answers  
    ⚡ Fast & Reliable  
    🎨 Simple & Elegant UI  
    """)

# Page Title
st.markdown('<p class="title">📄 Invoice Q&A Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🤖 Upload an invoice and ask a question about it.</p>', unsafe_allow_html=True)

# User Input
st.write("💡 **Enter your question:**")
input_text = st.text_input("", key="input", placeholder="E.g. What is the total amount on this invoice?")

# File Uploader for Image
st.markdown('<p class="upload-text">📸 Upload an Invoice Image</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

# Display Uploaded Image
image_data = None
if uploaded_file:
    image_data = input_image_setup(uploaded_file)
    st.image(image_data, caption="🖼️ Uploaded Invoice", use_column_width=True)

# Analyze Button
st.markdown("<br>", unsafe_allow_html=True)  # Line break for spacing
submit = st.button("🔍 Analyze Image")

# Processing
if submit:
    if not uploaded_file:
        st.error("⚠️ Please upload an invoice image first!")
    elif not input_text.strip():
        st.error("⚠️ Please enter a question!")
    else:
        st.success("✅ Processing your request... Please wait.")

        input_prompt = """
            You are an AI assistant specializing in invoice analysis. 
            You will receive an invoice image and a question. 
            Provide an accurate answer based on the invoice details.
        """
        response = get_gemini_response(input_prompt, image_data)

        st.subheader("💡 AI Response:")
        st.write(response)

# Footer - "Made By"
st.markdown('<p class="footer">🚀 Made with ❤️ by <b>Prarthana</b></p>', unsafe_allow_html=True)
