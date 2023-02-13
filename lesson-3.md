# 📓 Lesson 3 - NumPy

NumPy is a Python library that allows you to perform numerical processing. 

Here are some of the following features that NumPy can do:
- Supports N-dimensional array and matrix data structures
- Perform various mathematical operations on arrays and matrices
- Transposing and reshaping matrices
- Random number generation
- etc.

## 1. Installing NumPy

Let's start by installing NumPy that can be performed as follows:

```
pip install numpy
```

## 2. Using NumPy

To start using Numpy, we can import NumPy as follows:
```Python
import numpy as np
```

## 3. Data structures in NumPy

Let's consider a simple use case of NumPy for creating various data structures particularly tensors. Particularly, we'll use the `np.array()` method to create scalar, vector, matrix and a 3D tensor:
```Python
# Create a scalar (0D Tensor)
x1 = np.array(0)

# Create a vector (1D Tensor)
x2 = np.array([0, 1, 2])

# Create a matrix (2D Tensor)
x3 = np.array([0, 1, 2], [3, 4, 5], [6, 7, 8])

# Create a 3D Tensor
x4 = np.array([[[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8]],
               [[ 9, 10, 11],[12, 13, 14],[15, 16, 17]],
               [[18, 19, 20],[21, 22, 23],[24, 25, 26]]])
```

<p align="center">
  <img src="./img/lesson-3-numpy-tensor-illustration.png" width="50%">
</p>

As summarized above, a vector is an array of scalar, a matrix is an array of vectors and the 3D tensor is an array of matrix.

Now that we have taken a quick glance at NumPy, let's proceed to seeing how we can handle and process data.

