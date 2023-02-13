# 📓 Lesson 4 - Pandas

Pandas is a Python library that allows the loading, processing and wrangling of data. With Pandas you can gain access to data from a multitude of input sources such as CSV, TSV, Excel, SQL databases, JSON, etc. Afterwards, data can be exported out in the aforementioned formats as well.

## 1. Installing Pandas

Let's start by installing Pandas that can be performed as follows:

```
pip install pandas
```

## 2. Using Pandas

To start using Pandas, we can import Pandas as follows:
```Python
import pandas as pd
```

## 3. Read CSV data

Let's consider a simple use case of Pandas that I use quite often, which is to read in a CSV data:

```Python
df = pd.read_csv('data.csv')
```

In the above example, we are reading from a local file. However, if the CSV file is located on the cloud, it could also be read in a similar fashion. So instead of the file name, you can paste in the URL of the CSV file:

```Python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
```

To display the CSV data, this is as simple as calling the `df` variable:

```Python
df
```

which should yield the following DataFrame:

<p align="left">
  <img src="./img/lesson-4-pandas-df-output.png" width="59%">
</p>

As we can see, the DataFrame could be thought of as an $m×n$ matrix with $m$ rows and $n$ columns.

## 4. Selecting a single column

To select specific columns (such as the *MolWt* column) we can run the following:
```Python
df['MolLogP']
```
which produces the following Series output:
<p align="left">
  <img src="./img/lesson-4-pandas-select-columns.png" width="45%">
</p>

## 5. Selecting multiple columns

To select multiple columns (such as *MolWt* and *MolWt*) we can run the following:
```Python
df[['MolLogP','MolWt']]
```
which produces the following DataFrame output:
<p align="left">
  <img src="./img/lesson-4-pandas-select-multiple-columns.png" width="21%">
</p>
