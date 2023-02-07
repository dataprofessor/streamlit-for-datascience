# 📓 Lesson 1 - Getting up to speed with Streamlit

## 1.1. What is Streamlit?

Streamlit is a Python library you can use to build interactive data-driven web apps.

## 1.2. Prerequisite

Here's what you need to use Streamlit:
- Have basic Python knowledge.
- Write scripts to perform specific tasks (like taking several Excel files as input and combining them into one).
- Build and grow the Streamlit app line by line instead of starting with a predefined layout (it takes only a few lines of code).
If you can do all this, congratulations! You're ready to plunge into the world of Streamlit.

## 1.3. Setting up your Streamlit workspace

It is typically good practice to house the Streamlit app in their own dedicated conda environment. This way the library dependencies don’t get entangled with other Python libraries used by other apps.

Here, we're going to replicate a Streamlit app from an existing GitHub repo available at https://github.com/dataprofessor/eda-app/.

Particularly, we're going to clone the EDA app from a YouTube tutorial video on *How to Build an EDA app using Pandas Profiling*.

**Step 1.** Create a conda environment

Create a conda environment called eda:

```
conda create -n eda python=3.7.9
```

**Step 2.** Activate the eda environment:

```
conda activate eda
```

**Step 3.** Install prerequisite libraries by downloading the requirements.txt file (it contains the library version numbers):

```
wget https://raw.githubusercontent.com/dataprofessor/eda-app/main/requirements.txt
```




### Installing Streamlit

Streamlit can be installed using `pip` as shown below:

```
pip install streamlit
```

## 1.4. Creating your first Streamlit app

Before we get into the nuts and bolts of the Streamlit library, let's take a hands-on approach for learning how to use Streamlit. Particularly, creating a simple **Hello world app** would probably be an expected rite of passage to learning Streamlit!

It's not as difficult as you may think. In fact, it takes only 2 lines of code to do just that!

```Python
import streamlit as st
st.write('Hello world!')
```

Click on the **See code explanation** toggle button to reveal the explanatory text:

<details>
<summary>See code explanation</summary>

Here's a line-by-line breakdown of the code:
  1. Import the `streamlit` library as `st` (so that we can later refer to `streamlit` literally as `st` instead of having to type the full word `streamlit`.
  2. Use `st.write` to write a text output and inside the `st.write` command we use the `'Hello world!'` string as the input argument.
</details>

