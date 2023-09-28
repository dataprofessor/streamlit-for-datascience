import streamlit as st
import requests

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def read_md(md_file):
  img_url_path = 'https://github.com/dataprofessor/streamlit-for-datascience/blob/master'
  img_url_suffix = '?raw=true'
  
  md_url_path = 'https://raw.githubusercontent.com/dataprofessor/streamlit-for-datascience/master/content'
  md_lesson_url = f'{md_url_path}/{md_file}'
  response = requests.get(md_lesson_url)
  content = response.text
  content = content.replace('<img src="..', f'<img src="{img_url_path}').replace('" width', f'{img_url_suffix}" width')
  return content
