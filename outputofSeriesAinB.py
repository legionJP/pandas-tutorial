'''
Python Pandas Interview Questions
1. Can you get items of series A that are not available in another series B?
This can be achieved by using the ~ (not/negation symbol) and isin() method as shown below.
'''
import pandas as pd
df1 = pd.Series([2, 4, 8, 10, 12])
df2 = pd.Series([8, 12, 10, 15, 16])
df1=df1[~df1.isin(df2)]
print(df1)
"""
Output:
0    2
1    4
dtype: int64
"""
