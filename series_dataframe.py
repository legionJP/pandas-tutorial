import pandas as pd
import numpy as np

# Series
ser = pd.Series(np.random.rand(35))
print(ser)
type(ser)

# Data Frame 

df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334)) # 334 rows and 5 columns
print(df.head())
print(df)
print(df.dtypes)
print(df.describe())
#--------------------------------------------------------------------------#
# changing the data types to object 
df[0][0] = "Iam"
print(df.dtypes)
print(df.index)
print(df.columns)
df[0][0] = 0.696
# changing the data frame to numpy array
print(df.to_numpy())

# Doing the transpose of the data frame
print(df.T)
# it will transform the rows into columns and columns into rows

#--------------------------------------------------------------------------#
# Sorting the index of the data frame
print(df.sort_index(axis=1, ascending=False)) # it will sort the columns in descending order
# axis = 0 means rows and axis = 1 means columns

print(df[0]) # it will be a series 
print(type(df[0])) # so combination of series is a data frame


#--------------------------------------------------------------------------#

# View and Cpoy in Pandas

# View : It is just a reference to the original data frame means if we change the view it will change the original data frame
df1 = df
print(df1)

df1[0][0]= 0.3
print(df1)
print(df)
 # Note : whenn setting the value like this df1[0][0] = 0.3 it will give a warning but it will change the value, 
 # it is bcz it will not find the exact location of the value, so use loc or iloc to set the value

# Copy : It is a copy of the original data frame means if we change the copy it will not change the original data frame
df2 = df1[:]
df2[0][0] = 0.5
print(df)
print(df2)

# df loc and iloc
df.loc[0,0]=0.9
 # it will give the value at the 0th row and 0th column
#--------------------------------------------------------------------------#
df.columns = list("ABCDE")
print(df)
df.loc[0,"A"] = 341
df.loc[0,0] = 0.9
print(df)

df.drop(0,axis=1)
print(df)
# it will drop the 0th column
#--------------------------------------------------------------------------#

# returning the new data frame by loc 
newdf = df.loc[[1,2], ["C", "D"]]
print(newdf)
# all rows or coulumn
newdf = df.loc[[1,2], :]
print(newdf)

#--------------------------------------------------------------------------#


# Getting the complex dat frame by using 

print(df.loc[0]>0.3)
print(df.loc[(df[0]>0.3)])
print(df.loc[(df[0]>0.3) & df["A"]>0.1])

# loc is used to get the data frame by using the row and column names
# iloc is used to get the data frame by using the row and column index

print(df.iloc[0,4]) # using the 4th column  index and 0th row
print(df.iloc[[0,1], [1,2]]) # using the 0th and 1st row and 1st and 2nd column index

# Droping the rows and columns
newdf = df.drop(["A"] ,axis=1)
print(newdf)

# Ussing the inplace to drop the column from the original data frame
df.drop(["A"], axis=1, inplace=True)
print(df)

#--------------------------------------------------------------------------#

# reset_index 

df.reset_index(drop=True, inplace=True)


# dropna and fillna
df.loc[0,0] = np.nan
print(df)
print(df.dropna())
print(df.fillna(0))
print(df.fillna({0:0.5, 1:0.6}))

#--------------------------------------------------------------------------#

# isnull and notnull
print(df.isnull())
print(df.notnull())
df.loc[:,"A"] = np.random.rand(334)
#--------------------------------------------------------------------------#

# Groupby
# it is used to group the data frame by using the column name
data = {
    "name": ["Andy", "Doe", "John", "Doe"],
    "marks": [90, 89, 78, 89],
    "city": ["NY", "LA", "SF", "LA"]
}
df = pd.DataFrame(data)
print(df)
g = df.groupby("city")
print(g)

for city, city_df in g:
    print(city)
    print(city_df)

#--------------------------------------------------------------------------#

# Pandas Merging and Concatenation
# Concatenation : It is used to concatenate the data frames
# Merging : It is used to merge the data frames

df1 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})
df2 = pd.DataFrame({
    "A": [10, 11, 12],
    "B": [13, 14, 15],
    "C": [16, 17, 18]
})

print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))

#--------------------------------------------------------------------------#

# Droping the duplicate values
data = {
    "name": ["Andy", "Doe", "John", "Doe"],
    "marks": [90, 89, 78, 89],
    "city": ["NY", "LA", "SF", "LA"]
}
df = pd.DataFrame(data)
print(df)
print(df.duplicated())
print(df.drop_duplicates())
print(df.drop_duplicates(subset=["name"], keep="last"))

print(df.shape)
print(df.info())

print(df['name'].value_counts(dropna=False))


# -------------------------------------------------------------------------------#
# datarame which contains the 3 rows and 2 columns

df = pd.DataFrame(np.random.rand(3,2), index=[1,2,3], columns=["A","B"])
print(df)
print(df.describe())
print(df.mean())
print(df.std())
print(df.median())
print(df.mode())
print(df.var())
print(df.sum())
print(df.corr())


# Doing the union of the dataseries
import pandas as pd
import numpy as np
df1 = pd.Series([2, 4, 5, 8, 10])
df2 = pd.Series([8, 10, 13, 15, 17])
p_union = pd.Series(np.union1d(df1, df2))  # union of series
p_intersect = pd.Series(np.intersect1d(df1, df2))  # intersection of series
unique_elements = p_union[~p_union.isin(p_intersect)]
print(unique_elements)
"""
Output:
0     2
1     4
2     5
5    13
6    15
"""
