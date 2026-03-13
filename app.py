import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="My Gemini Web App", layout="centered")
st.title("🤖 Public Gemini AI")

# Sidebar for the API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        user_input = st.text_input("Ask Gemini anything:", placeholder="Type here...")
        
        if st.button("Generate Response"):
            if user_input:
                with st.spinner("Gemini is thinking..."):
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=user_input
                    )
                    st.markdown("### Response:")
                    st.write(response.text)
            else:
                st.warning("Please type something first!")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("AIzaSyBPM2P8IR3QxvA48da2DKoq_1hObZ1b3Uo.")
  
