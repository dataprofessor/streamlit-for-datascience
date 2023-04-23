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

## Creating a basic plot using Matplotlib

Let's start by creating a simple plot using Matplotlib. 

## Line graph
Here, we're going to plot a simple line graph that shows the population growth of a hypothetical city over time using the following code:

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
<details>
  <summary><i>See code explanation</i></summary>

Here's a line-by-line breakdown of the code:
  1. Import the `matplotlib.pyplot` as `plt` (so that we can later refer to `matplotlib.pyplot` literally as `plt` instead of having to type the full version of `matplotlib.pyplot`.
  2. Create `years` and `population` variables that will be used for subsequent steps in creating the plot.
  3. Create the plot via `plt.plot()` and specifying `years` and `population` as input arguments. This will create a line plot.
  4. Finally, we're going to display the plot via `plt.show()`.
</details>

This gives us the following plot:

<p align="left">
  <img src="../img/lesson-6-matplotlib-simple-line-plot.png" height="300">
</p>


## Adding labels


