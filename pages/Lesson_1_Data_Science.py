import streamlit as st
import pandas as pd
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 1 - Getting up to speed with Data Science", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-1.md')
st.markdown(md, unsafe_allow_html=True)
