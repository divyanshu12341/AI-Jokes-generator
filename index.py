from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
load_dotenv()
import os
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
st.title("AI Joke generator")
st.write("Type a topic and get a funny joke instantly!")
st.sidebar.header("Configuration")
tone = st.sidebar.selectbox(
    "SELECT TONE",["Witty","Wholesome","Sarcastic","Dad Joke Style"]
)
subject = st.text_input("What should be the joke be about","")
if(st.button("Generate Joke")):
    with st.spinner("Generating your Joke ..."):
        prompt = ChatPromptTemplate.from_messages([
            ("system","You are comedian who speaks in {tone}"),
            ("human","Tell me the short joke about {subject}")
        ])
        model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
        chain = prompt|model|StrOutputParser()
        result = chain.invoke({"tone":tone,"subject":subject})
        st.subheader("Here is your joke: ")
        st.success(result)