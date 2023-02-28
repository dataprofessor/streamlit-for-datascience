import streamlit as st
from PIL import Image
import glob
import os
import base64
from pathlib import Path
from utilities import load_bootstrap

# Image display
load_bootstrap()
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

def update_params():
    st.experimental_set_query_params(course=st.session_state.lesson)

md_files = sorted([int(x.strip('Lesson-').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('./img/logo.png'))


lesson_list = [f'Lesson {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["course"][0] in lesson_list:
    st.session_state.lesson = query_params["course"][0]

selected_day = st.selectbox('Select a Lesson 👇', lesson_list, key="lesson", on_change=update_params)

#####

# Display content
url_prefix = os.getcwd()
    
for i in lesson_list:
    if selected_day == i:
        #st.markdown(f'# 🗓️ {i}')
        j = i.replace(' ', '-')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read(), unsafe_allow_html=True)


            

img_url = 'https://raw.githubusercontent.com/dataprofessor/streamlit-for-datascience/master/img/lesson-2-data-science-life-cycle.png?token=GHSAT0AAAAAAB64ZU57RECHN24WZG47SZPQY76GAJQ'
img_html = f'<img src={img_url}>'
st.markdown(img_url, unsafe_allow_html=True)
