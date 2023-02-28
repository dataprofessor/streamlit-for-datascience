import streamlit as st
from PIL import Image
import glob
import os

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
            st.markdown(f.read().replace('<img src="../img', f'<img src="{url_prefix}/img'), unsafe_allow_html=True)
            st.write(os.listdir(os.getcwd()))
            st.write(os.path.relpath())
