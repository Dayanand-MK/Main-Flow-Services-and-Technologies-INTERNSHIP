# LEARN HOW TO READ CSV FILES AND MANIPULATE DATA FRAMES USING PANDAS.

import pandas as p

data = p.read_csv("01.Data Cleaning and Preprocessing.csv")

print("\n**********TYPE**********\n")
print(type(data))

print("\n**********INFO**********\n")
print(data.info())

print("\n**********DESCRIBE**********\n")
print(data.describe())