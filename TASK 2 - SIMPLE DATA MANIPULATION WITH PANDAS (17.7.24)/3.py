# PRACTICE BASIC DATA MANIPULATION OPERATIONS LIKE FILTERING, SORTING, AND GROUPING DATA.

import numpy as np
from scipy import stats
import pandas as p

data = p.read_csv("01.Data Cleaning and Preprocessing.csv")

a=data.columns
print(a)

data.drop(['Observation'],axis=1,inplace = True)
b = data.columns
print(b)

q1 = data.quantile(0.25)
q2 = data.quantile(0.75)
I = q2-q1
print(I)

data1 = data[~((data<(q1-1.5*I))|(data>(q2+1.5*I))).any(axis=1)]
print(data1)