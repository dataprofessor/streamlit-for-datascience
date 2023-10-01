import streamlit as st
import pandas as pd
from utilities import load_css, read_md

st.set_page_config(page_title="Project 1 - Using NumPy in Streamlit", page_icon="📖", layout="wide")

load_css()

md = read_md('Project-1.md')
st.markdown(md, unsafe_allow_html=True)
