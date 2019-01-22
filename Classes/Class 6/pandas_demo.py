import numpy as np
import pandas as pd

# https://www.tutorialspoint.com/python_pandas
# Pandas is a huge library for Data Science and Data Management
# Has a lot of functionality of numpy and sql
# We will just go through the basic accessing operations

# Data types in Pandas
# Series 1D
# Data Frames 2D
# Panel 3D

s = pd.Series(np.arange(5, 0, -1))
print(s, "\n")

df = pd.DataFrame([(a, a * a) for a in range(5)],
                  dtype="i1",
                  columns=["Number", "Square"])
# if columns is not specified, default column names of 0, 1 ... etc are given
print(df, "\n")

# Specifying the column names gives a series of the column
print(type(df["Square"]))
print(df["Square"], "\n")

# iloc gives you a row as a series
print(type(df.iloc[0]))
print(df.iloc[0], "\n")

# To access a particular cell
print(type(df["Square"].iloc[2]))
print(df["Square"].iloc[2], "\n")

file_name = "example.csv"
# To read a file as a DataFrame
data = pd.read_csv(file_name)

# To save a file from a DataFrame
data.to_csv("save_example.csv", index=False)
# index=False will exclude the row numbers from being saved to a file

# To read a file as a numpy array
data = pd.read_csv(file_name).values

# To read a file as a list
data = pd.read_csv(file_name).values.tolist()
# Note that the DataFrame is being converted to a ndarray and then to a list

