import streamlit as st
from langchain_community.llms import Ollama
import pandas as pd

llm = Ollama(model="llama3")
st.title("Llama3 chatbot")

prompt = st.text_area("Enter here: ")

if st.button("Prompt"):
    if prompt:
        with st.spinner("Generating ... "):
            st.write(llm.invoke(prompt, stop=['<|eot_id|>']))