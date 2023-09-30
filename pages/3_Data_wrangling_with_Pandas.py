import streamlit as st
import pandas as pd
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 3 - Data wrangling with Pandas", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-3.md')
st.markdown(md, unsafe_allow_html=True)
