import streamlit as st
import pandas as pd
from utilities import load_css, read_md

st.set_page_config(page_title="Project 4 - Using Matplotlib to create a plot in Streamlit", page_icon="🛠️", layout="wide")

load_css()

md = read_md('Project-4.md')
st.markdown(md, unsafe_allow_html=True)
