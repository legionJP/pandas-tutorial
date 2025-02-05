# pandas read_excel 
import pandas as pd
import numpy as np

df = pd.read_excel('sheet1.xlsx')
print(df)

data = pd.read_excel('sheet1.xlsl', sheet_name='sheet2')
print(data)