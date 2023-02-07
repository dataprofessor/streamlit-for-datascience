# 📓 Lesson 1 - Getting up to speed with Streamlit

## Installing Streamlit

Streamlit can be installed using `pip` as shown below:

```
pip install streamlit
```

## Creating your first Streamlit app

Before we get into the nuts and bolts of the Streamlit library, let's take a hands-on approach for learning how to use Streamlit. Particularly, creating a simple **Hello world app** would probably be an expected rite of passage to learning Streamlit!

It's not as difficult as you may think. In fact, it takes only 2 lines of code to do just that!

Click on the **See code** toggle button to reveal the code box:

```Python
import streamlit as st
st.write('Hello world!')
```

<details>
<summary>See code explanation</summary>

```
Here's a line-by-line breakdown of the code:
  1. Import the `streamlit` library as `st` (so that we can later refer to `streamlit` literally as `st` instead of having to type the full word `streamlit`.
  2. Use `st.write` to write a text output and inside the `st.write` command we use the `'Hello world!'` string as the input argument.
```
</details>

