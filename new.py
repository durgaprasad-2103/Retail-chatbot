from langchain_community.llms import GooglePalm
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()

llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    response = llm(question)

    st.header("Answer")
    st.write(response)