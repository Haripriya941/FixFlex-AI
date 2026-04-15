import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyC6APfVhtfxPOpyKjrKk_z-fbdzbDML6ds")
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="FixFlex AI")
st.title("🤖 FIXFLEX AI")

st.write("Upload ticket image or type your issue. AI will analyze and give step-by-step solution.")

uploaded_image = st.file_uploader("Upload Ticket Image", type=["jpg", "jpeg", "png", "webp"])

user_input = st.text_input("Enter your issue")

context = """
You are an AI Customer Support Agent.

Your job:
1. Analyze the issue from text or image
2. Identify sentiment
3. Identify issue type
4. Provide a STEP-BY-STEP solution to solve the problem

Response format STRICTLY:

Sentiment:
Issue:

Step-by-Step Solution:
Step 1:
Step 2:
Step 3:
Step 4:

Final Suggestion:
"""

if st.button("Submit"):

    if uploaded_image is None and user_input.strip() == "":
        st.warning("Please upload an image or enter your issue")
    else:
        with st.spinner("Analyzing..."):

            if uploaded_image is not None:
                img = Image.open(uploaded_image)
                response = model.gener4ate_content([img, user_input, context])
            else:
                response = model.generate_content(context + user_input)
            st.subheader(" AI Support Response")
            st.write(response.text)