# 📓 Lesson 6 - Data Visualization with Matplotlib

<p align="center">
  <img src="https://matplotlib.org/_static/logo_light.svg" width="300">
</p>

Data visualization is an important topic that allows us to represent complex data in a visually appealing and summarized manner. We often hear that a picture is worth a thousand words and this could be said for visualizations of data.

In this lesson, we're going to create some data visualizations using the `Matplotlib` library.

## Installing Matplotlib

Firstly, open up a terminal window and install Matplotlib via pip as follows:
```
pip install matplotlib
```

## Creating a basic plot

Let's start by creating a simple plot using Matplotlib. 

Here, we're going to plot a simple line graph that shows the population growth of a hypothetical city over time.

```python
import matplotlib.pyplot as plt

# Data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
population = [2.5, 3.0, 3.7, 4.5, 5.3, 6.1, 6.9, 7.7]

# Create plot
plt.plot(years, population)

# Show plot
plt.show()
```

<p align="left">
  <img src="../img/lesson-6-matplotlib-simple-line-plot.png" height="534">
</p>
