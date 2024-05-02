"""
app.py
"""
import streamlit as st
from openai import OpenAI

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
ASSISTANT_ID = st.secrets["ASSISTANT_ID"]