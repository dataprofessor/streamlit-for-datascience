# 📓 Lesson 2 - Getting up to speed with Data Science

## Table of Contents
1. [What is Data Science?](#1-what-is-data-science)
2. [Process of data science](#2-process-of-data-science)
3. [Hardware for Data Science](#3-hardware-for-data-science)
4. [Toolkits for Data Science](#4-toolkits-for-data-science)

## 1. What is Data Science?

Data science boils down to the conversion of data to knowledge and insights. At a high-level, the science of data science implies that we're appying the scientific methodology to tackle data problems that essentially starts with the formulation of a working hypothesis or initial assumptions that you have. From there, you can decide which particular data to collect and perform the analysis.

## 2. Process of data science

This involves a series of steps and the typical data science process can best be summarized by data frameworks such as [OSEMN](https://web.archive.org/web/20211219192027/http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) that encompasses the following steps involving data:
- **Obtain** - Any data projects essentially starts with access to data and one can do this by compiling a dataset based on objectives of projects.
- **Scrub** - Raw data is often messy, pre-mature and not suitable for data analysis. As a result, one must first pre-process the data such that any missing data and inconsistencies are addressed so that they are amenable for further analysis.
- **Explore** - In order to discover any meaningful insights from the data, exploring the data is often a great first step to gain an understanding of the data. This will allow the practitioner to make a well-informed decision on the next steps for further data exploration or which subset of data to used for further analysis. In some circumstances, one may discover that additional data needs to be collected.
- **Model** - Once data has been prepared and curated, the typical next steps would be to take the data and build a machine learning model that can be used to make predictions on new data.
- **iNterpret** - Probably the most impactful part is the intrepretation of the model where useful knowledge and insights are extracted from models. It should be noted that the most sophisticated machine learning algorithm may not be the best algorithm as they may not afford interpretability whereas simple algorithms such as linear regression or decision tree may provide more interpretability.

Taking a step back for a high-level overview of a typical data project can be summarized by the following data life cycle:

<br>
  <p align="center">
    <img src="../img/lesson-2-data-science-life-cycle.png" width="60%">
  </p>
<br>
  
## 3. Hardware for Data Science

Fundamentally, any hardware that you have access to will be sufficient for the purpose of writing code, perform analysis and testing the creation of Streamlit apps. This can be a laptop, desktop or a computer hosted on the cloud. Such computers could run on a variety of operating systems including Windows, Mac OSX or Linux.

On top of these hardware, just make sure to have a working [Python](https://www.python.org/) environment and we're good to go.


## 4. Toolkits for Data Science

Now that we have a fundamental knowledge of data science and the hardware, let's take a look at the tools of the trade.

Common toolkits that are helpful for any data science projects includes the following:
Python library | Brief description | OSEMN phase
---|---|---
`NumPy` | Numerical processing | Scrub
`Pandas` | Data wrangling | Scrub
`Matplotlib` | Data visualization | Explore
`Scikit-learn` | Machine learning | Model / iNterpret

These toolkits provide ready-to-use functions that can be readily harnessed to retrieve, prepare, visualize and analyze data. Without such toolkits we would have to implement our own custom functions to do the same tasks.

### NumPy
[NumPy](https://numpy.org/) is a Python library for numerical computing by allowing one to work with arrays and matrices of numerical data. NumPy is helpful for data science work because it allows for efficient manipulation and computation of large arrays of data.

### Pandas
[Pandas](https://pandas.pydata.org/) is a popular Python library for performing data wrangling and analysis in Python. It provides data structures (*e.g.* DataFrame and Series) for storing and querying data. Pandas also provides a wide range of functions for data cleaning, transformation, and analysis, thereby making it a powerful tool for performing exploratory data analysis and visualization.

### Matplotlib

[Matplotlib](https://matplotlib.org/) is an established plotting library in Python. One can use Matplotlib to create a variety of data visualizations including line plots, scatter plots, histograms, and several others. Matplotlib is helpful for data science work because it allows the creation of high-quality visualizations of data as well as enabling understanding of data patterns and relationships. Additionally, [Seaborn](https://seaborn.pydata.org/), [Plotly](https://plotly.com/) and Altair are other popular plotting libraries that one can also use for data visualization. 

### Scikit-learn

[Scikit-learn](https://scikit-learn.org/) is a machine learning library in Python that provide tools for classification, regression, clustering, dimensionality reduction, model selection as well as preprocessing. Scikit-learn is helpful for data science work because it enables data preprocessing, model building and model analysis where insights can be drawn and predictions can be made.

## Summary

In this lesson, we've taken a high-level look at data science as well as the computing hardware and software for doing data science.
