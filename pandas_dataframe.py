import numpy as np
import pandas as pd

dict1 = {
    "name": ["Andy", "Doe", "John", "Doe"],
    "marks": [90, 89, 78, 89],
    "city": ["NY", "LA", "SF", "LA"]
}

df = pd.DataFrame(dict1)
print(df)

#-------------------------------------------------------------------------------#
# Exporting dataframes to csv

df.to_csv("friends.csv")
df.to_csv("friends_index_false.csv", index=False)

print(df.head(2))
print(df.tail(2))
print(df.describe())

#-------------------------------------------------------------------------------#

# Reading the CSV File: 
jp = pd.read_csv("friends.csv")
print(jp)
print(jp["marks"])

jp["marks"][0] = 98
print(jp["marks"][0])    
jp.to_csv("jp1.csv")

jp.index = ["first", "second", "third", "fourth"]
print(jp)
# -----------------------------------------#

# DataFrame 
'''
class DataFrame()
Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Data structure also contains labeled axes (rows and columns).
 Arithmetic operations align on both row and column labels.
   Can be thought of as a dict-like container for Series objects.
The primary pandas data structure.

Parameters
data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
    Dict can contain Series, arrays, constants, dataclass or list-like objects.
      If data is a dict, column order follows insertion-order. 
      If a dict contains Series which have an index defined, 
      it is aligned by its index. This alignment also occurs 
      if data is a Series or a DataFrame itself. 
    Alignment is done on Series/DataFrame inputs.
'''