
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit page configuration
st.set_page_config(page_title="Gemini Invoice Analyzer", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Style the button */
        .stButton>button {
            background-color: #FF0000; /* Red */
            color: white; 
            border-radius: 8px; 
            font-size: 16px; 
            padding: 10px 20px;
            border: none;
        }

        /* Change button color to black on hover */
        .stButton>button:hover {
            background-color: #000000; /* Black */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.image("img.png", width=300)
st.sidebar.title("💡 About This App")
st.sidebar.write("This app analyzes invoice images and extracts relevant information using Gemini AI.")
st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 **Developed by:** Prarthana Singh")
st.sidebar.write("📧 **Contact:** prarthanas645@email.com")

# Main UI
st.title("📄 Gemini Invoice Analyzer")
st.write("Upload an invoice image and ask questions about it.")

input = st.text_input("Enter your question:", placeholder="e.g., What is the total amount on this invoice?")
uploaded_file = st.file_uploader("Upload an invoice image (JPG, JPEG, PNG):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Analyze Invoice 🧾")

if submit and uploaded_file:
    with st.spinner("Processing the image... 🕒"):
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response("You are an expert in invoices.", image_data, input)
        st.success("✅ Analysis Complete!")
        st.subheader("🔍 Extracted Information:")
        st.write(response)
else:
    st.warning("⚠️ Please upload an image and enter a question.")
