import pandas as pd

# df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
# #Select data using label-based indexing
# print(df.loc[0, "A"])
# #Select data using position-based indexing
# print(df.iloc[0,1])

std_data = [
    (1, 'varun', 30, 'male', 'chandigarh'),
    (2, 'ram', 31, 'male', 'delhi'),
    (3, 'david', 28, 'male', 'himachal'),
]
df = pd.DataFrame(std_data, columns =["stud_id", "name", "age", "gender", "address"])
print(df)
