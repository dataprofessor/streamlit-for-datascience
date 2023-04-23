import streamlit as st
import streamlit.components.v1 as components
import markdown as md
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
            page_content = f.read().replace('../img', 'app/img')
            html_content = md.markdown(page_content)
            components.html(html_content)
            #st.markdown(page_content, unsafe_allow_html=True)
            


#st.markdown("![](lesson-1-streamlit-workflow.png)", unsafe_allow_html=True)

#img_url = 'https://raw.githubusercontent.com/dataprofessor/30days/master/content/images/2C9104F7-CF84-4DAF-9004-52BB4644CF28.png'
#img_html = f'<img src={img_url} width="500">'
#st.markdown(img_html, unsafe_allow_html=True)
