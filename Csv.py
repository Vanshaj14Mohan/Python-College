import pandas as pd
import numpy as np

# df = pd.read_excel("C:/Users/HP/Documents/student.xlsx")
df = pd.read_excel("student.xlsx")
print(df)
#for top
print(df.head())
# print(df.head(2))
#For bottom
print(df.tail())
print(df.tail(2))
# print(df.tail(2))
#for shape
print(df.shape)
#for rows & columns
print(df.size)
print(df.columns)
print(df.values)
# print(df.index)
# print(df.info)
print(df.dtypes)
 