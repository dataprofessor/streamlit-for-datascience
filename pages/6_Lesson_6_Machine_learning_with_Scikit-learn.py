import streamlit as st
import pandas as pd
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 6 - Machine Learning with Scikit-learn", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-6.md')
st.markdown(md, unsafe_allow_html=True)
