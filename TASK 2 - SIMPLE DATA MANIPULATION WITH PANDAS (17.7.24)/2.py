# PERFORM SIMPLE DATA CLEANING TASKS SUCH AS HANDLING MISSING VALUES AND REMOVING DUPLICATES.
import pandas as p

data = p.read_csv("01.Data Cleaning and Preprocessing.csv")

print("\n**********DUPLICATE**********\n")
data1 = data.drop_duplicates()
print(data1)

print("\n**********NULL**********\n")
data2 = data.isnull()
print(data2)

print("\n**********NULL.SUM**********\n")
data3 = data.isnull().sum()
print(data3)

print("\n**********NOTNULL**********\n")
data4 = data.notnull()
print(data4)

print("\n**********NULL.SUM.SUM**********\n")
data5 = data.isnull().sum().sum()
print(data5)

print("\n**********HANDLING METHOD 1**********\n")
data6 = data.fillna(value = 0)
print(data6)

print("\n**********HANDLING METHOD 2**********\n")
data7 = data.fillna(method = "pad")
print(data7)

print("\n**********HANDLING METHOD 3**********\n")
data8 = data.fillna(method = "bfill")
print(data8)