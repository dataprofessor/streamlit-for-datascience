# 📓 Lesson 7 - Machine Learning with Scikit-learn

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="300">
</p>

The Scikit-learn library is the gold standard in performing machine learning in Python as it allows you to build machine learning models, prepare data, analyze data, and evaluate models. As the tool has been around for quite some time since 2007, there are extensive examples and resources that one can use to get started.

In this lesson, we're going to use the `Scikit-learn` library for the various phases in the data science cycle as mentioned earlier (e.g. build machine learning models, prepare data, analyze data, and evaluate models).

## Installing Scikit-learn

Firstly, open up a terminal window and install Scikit-learn via pip as follows:
```
pip install scikit-learn
```

## Data representation used in Scikit-learn 

We'll start with the basics by examining Scikit-learn's tabular representation of data.

The tabular dataset for a supervised learning problem will contain both **X** and **Y** variables, while the tabular dataset for an unsupervised learning problem will contain only **X** variables.

As an overview, **X** variables are also known as independent variables, and they can describe samples of interest quantitatively or qualitatively, while **Y** variables are known as dependent variables, and they serve as target or response variables used in predictive models.

<p align="center">
  <img src="../img/lesson-7-scikit-learn-tabular-data.png" width="550">
</p>

To illustrate, if we're constructing a model to predict whether individuals will have a disease or not, the disease/non-disease status is the y variable and clinical test results are the X variable.

## Loading data from a CSV file

A dataset can be stored as a CSV file and read using the Pandas library via the `pd.read_csv()` function. Hence, a Pandas DataFrame is used to represent the loaded data.

In the following example, we're loading in a CSV stored on the cloud in the GitHub repo.

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
df
```

<p align="center">
  <img src="../img/lesson-7-scikit-learn-load-data.png" width="400">
</p>

