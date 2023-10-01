## 🎨 Project 3 - Using Pandas for EDA in Streamlit

### What are we building?
Let's now use Pandas to perform EDA in a Streamlit app. Particularly, we're going to create an app that will allow us to load in a CSV data and perform a quick EDA analysis of the data.

### How the code works?
Here's an explanation of the code in a step-by-step manner:
1. Import necessary libraries
2. Display the title of the app
3. Load and display a CSV file as DataFrame
4. Create a conditional button that displays a DataFrame of a descriptive statistics analysis upon clicking on the `Show descriptive statistics analysis` button

### Code
```Python
import streamlit as st
import pandas as pd

st.title('🐼 Pandas - An EDA example')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
st.write(df)
  
if st.button('Show descriptive statistics analysis'):
  st.write(df.describe())
else:
  st.info('👆 Click on the button ')
```

### Completed app
The above code gives us the following Streamlit app ([GitHub repo](https://github.com/dataprofessor/st-pandas-example-2) | [Demo app](https://dataprofessor-st-pandas-example-2-streamlit-app-8ywtu6.streamlit.app))

<p align="left">
  <img src="../img/lesson-5-pandas-eda-example-streamlit-app.gif" width="80%">
</p>

### Homework
Now that you have this Pandas app completed, can you build upon this Streamlit app by adding input widgets that will allow users to select one of many EDA statistical analysis of their choice. After selection of the analysis option to perform, the app will conditionally display the corresponding output.

> 📣 **Learn in Public:** 
> 
> Share your solution (the updated Streamlit app) on social media (Twitter and/or LinkedIn) and tag us (`@streamlit`).
