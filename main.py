import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Simple Generative AI Chatbot")

if not openai.api_key:
    st.error("OpenAI API key not found. Please add it to your .env file as OPENAI_API_KEY.")
else:
    user_input = st.text_input("Ask me anything:")

    if user_input:
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
                max_tokens=100,
            )
            bot_response = response.choices[0].message.content.strip()
            st.write("🤖", bot_response)
        except Exception as e:
            st.error(f"Error: {e}")
