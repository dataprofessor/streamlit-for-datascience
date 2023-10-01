import streamlit as st
from PIL import Image
from utilities import load_css
# from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Welcome to the Streamlit for Data Science course",
    page_icon="🏠",
)

load_css()

img = Image.open('img/streamlit-datascience-course-logo.png')
st.image(img)

# About
st.header('About')
st.info('The Streamlit for Data Science course will show you how to use Streamlit to prepare and analyze data as well as embed data visualizations and machine learning models right inside the Streamlit app. The best part of is that you can use various input and output widgets to make the app interactive and data-driven! Finally you can deploy the Streamlit app to the cloud and share with the community.')

# Table of Contents
# st.header('Table of Contents')



baseURL = 'https://datascience-course.streamlit.app/'

lessonURL = {
    0: 'Lesson_0_Intro_to_Streamlit',
    1: 'Lesson_1_Intro_to_Data_Science',
    2: 'Lesson_2_Numerical_processing_with_NumPy',
    3: 'Lesson_3_Data_wrangling_with_Pandas',
    4: 'Lesson_4_Exploratory_data_analysis_with_Pandas',
    5: 'Lesson_5_Data_visualization_with_Matplotlib',
    6: 'Lesson_6_Machine_learning_with_Scikit-learn',
    7: 'Project_1_NumPy_in_Streamlit',
    8: 'Project_2_Pandas_in_Streamlit',
    9: 'Project_3_Pandas_for_EDA_in_Streamlit',
    10: 'Project_4_Matplotlib_in_Streamlit',
    11: 'Project_5_Scikit-learn_in_Streamlit',
}

lessonName = {
    0: 'Lesson 0 - Getting up to speed with Streamlit',
    1: 'Lesson 1 - Getting up to speed with Data Science',
    2: 'Lesson 2 - Numerical processing with NumPy',
    3: 'Lesson 3 - Data wrangling with Pandas',
    4: 'Lesson 4 - Exploratory Data Analysis with Pandas',
    5: 'Lesson 5 - Data Visualization with Matplotlib',
    6: 'Lesson 6 - Machine Learning with Scikit-learn',
    7: 'Project 1 - Using NumPy in Streamlit',
    8: 'Project 2 - Using Pandas in Streamlit',
    9: 'Project 3 - Using Pandas for EDA in Streamlit',
    10: 'Project 4 - Using Matplotlib to create a plot in Streamlit',
    11: 'Project 5 - Using Scikit-learn to create an ML model in Streamlit',
}


st.markdown(f'''

  <h3>Table of Contents</h3>
  
<div class="sidebar">
  <a href="/">Home</a>
  <a href="{lessonURL[0]}" target="_self">lessonName[0]</a>
  <a href="{lessonURL[1]}">lessonName[1]</a>
  <a href="{lessonURL[2]}">lessonName[2]</a>
  <a href="{lessonURL[3]}">lessonName[3]</a>
  <a href="{lessonURL[4]}">lessonName[4]</a>
  <a href="{lessonURL[5]}">lessonName[5]</a>
  <a href="{lessonURL[6]}">lessonName[6]</a>
  <a href="{lessonURL[7]}">lessonName[7]</a>
  <a href="{lessonURL[8]}">lessonName[8]</a>
  <a href="{lessonURL[9]}">lessonName[9]</a>
  <a href="{lessonURL[10]}">lessonName[10]</a>
  <a href="{lessonURL[11]}">lessonName[11]</a>
</div>
''', unsafe_allow_html=True)


#if st.button('**Lesson 0** - Getting up to speed with Streamlit'):
#    switch_page('Lesson_0_Intro_to_Streamlit')
  
#if st.button('**Lesson 1** - Getting up to speed with Data Science'):
#    switch_page('Lesson_1_Intro_to_Data_Science')
  
#if st.button('**Lesson 2** - Numerical processing with NumPy'):
#    switch_page('Lesson_2_Numerical_processing_with_NumPy')
  
#if st.button('**Lesson 3** - Data wrangling with Pandas'):
#    switch_page('Lesson_3_Data_wrangling_with_Pandas')
  
#if st.button('**Lesson 4** - Exploratory Data Analysis with Pandas'):
#    switch_page('Lesson_4_Exploratory_data_analysis_with_Pandas')
  
#if st.button('**Lesson 5** - Data Visualization with Matplotlib'):
#    switch_page('Lesson_5_Data_visualization_with_Matplotlib')
  
#if st.button('**Lesson 6** - Machine Learning with Scikit-learn'):
#    switch_page('Lesson_6_Machine_learning_with_Scikit-learn')  
  
#if st.button('**Project 1** - Using NumPy in Streamlit'):
#    switch_page('Project_1_NumPy_in_Streamlit')
  
#if st.button('**Project 2** - Using Pandas in Streamlit'):
#    switch_page('Project_2_Pandas_in_Streamlit')
  
#if st.button('**Project 3** - Using Pandas for EDA in Streamlit'):
#    switch_page('Project_3_Pandas_for_EDA_in_Streamlit')
  
#if st.button('**Project 4** - Using Matplotlib to create a plot in Streamlit'):
#    switch_page('Project_4_Matplotlib_in_Streamlit')

#if st.button('**Project 5** - Using Scikit-learn to create an ML model in Streamlit'):
#    switch_page('Project_5_Scikit-learn_in_Streamlit')
