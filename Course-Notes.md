# Week 1 Notes

## Book to Use for Course
- Python for Data Analysis - Wes McKinney

## Linux commands
 REPL - Read, Execute, Print, Loop
 
 `uname -a` - Prints the name, version and other details about the current machine and the operating system running on it
 
`python test.py` - Runs a Python application

`touch test2.py` - Creates a new file

## Miscellaneous

- Jupyter - Julia + Python + R


---
# Python for Data Analysis Notes

## Chapter 1 

---
### *NumPy*
>Short for Numerical Python

>Provides the data structures, algorithms, and library glue needed for most scientific applications involving numerical data in Python
#### **Primary Features**
- A fast and efficient multidimensional array object ndarray
- Functions for performing element-wise computations with arrays or mathematical operations between arrays
- Tools for reading and writing array-based datasets to disk
- Linear algebra operations, Fourier transform, and random number generation
- A mature C API to enable Python extensions and native C or C++ code to access NumPy’s data structures and computational facilities

---
### *pandas*
>Provides high-level data structures and functions designed to make working with structured or tabular data fast, easy, and expressive
#### **Primary Features**
- DataFrame: a tabular, column-oriented data structure with both row and column labels
- Series: a one-dimensional labeled array object

---
### *matplotlib*
>Produces plots and other two dimensional data visualizations.

---
### *SciPy*
>Collection of packages to address a number of different standard problem domains in scientific computing.

---
### *scikit-learn*
>General purpose machine learning toolkit for Python programmers
#### **Primary Features**
- Classification: SVM, nearest neighbors, random forest, logistic regression, etc.
- Regression: Lasso, ridge regression, etc.
- Clustering: k-means, spectral clustering, etc.
- Dimensionality reduction: PCA, feature selection, matrix factorization, etc.
- Model selection: Grid search, cross-validation, metrics
- Preprocessing: Feature extraction, normalization

---
### *statsmodels*
>Statistical analysis package with algorithms for classical statistics and econometrics
#### **Primary Features**
- Regression models: Linear regression, generalized linear models, robust linear models, linear mixed effects models, etc.
- Analysis of variance (ANOVA)
- Time series analysis: AR, ARMA, ARIMA, VAR, and other models
- Nonparametric methods: Kernel density estimation, kernel regression
 - Visualization of statistical model results

---
### Installing or Updating Python Packages

```
pip install package_name
pip install --upgrade package_name
```

---
### Import Conventions

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```

## Chapter 2

### Python Interpreter

`python` - start python interpreter from a terminal command line

`python program.py` - run python program

### IPython Shell

`ipython` - start Interactive Python shell from a terminal command line

### Jupyter Notebook

`jupyter notebook` - start Jupyter from a terminal command line

Note: use --no-browser option or it will start in default web browser (http://localhost:8888)

### Stuff to know

Tab Completion - While entering expressions in the shell, pressing the Tab key will search the namespace for any variables (objects, functions, etc.) matching the characters typed so far

Introspection - Using a question mark (?) before or after a variable will display some general information about the object

`%run file` - run any file as a Python program inside the environment of an IPython session

`%load script` - imports a script into a code cell in a Jupyter notebook

`%paste` - takes whatever text is in the clipboard and executes it as a single block in the shell

`%cpaste` - allows for looking at the pasted code before executing it (use Ctl-C to break out of execution)

### Exercises

See **Practice-01.ipynb**
