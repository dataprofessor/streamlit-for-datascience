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

st.markdown('''

  <h3>Table of Contents</h3>
  
<div class="sidebar">
  <a href="#state-of-llm-apps-2023">Top</a>
  <a href="#about-the-report">About the Report</a>
  <a href="#key-takeaways">Key Takeaways</a>
  <a href="#key-concerns">Key Concerns</a>
  <a href="#llm-tool-popularity">LLM Tool Popularity</a>
  <a href="#llm-at-a-glance">LLM at a Glance</a>
  <a href="#llm-app-gallery">LLM App Gallery</a>
  <a href="#llm-models">LLM Models</a>
  <a href="#vector-databases">Vector Databases</a>
  <a href="#llm-orchestration">LLM Orchestration</a>
  <a href="#methodology">Methodology</a>
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
