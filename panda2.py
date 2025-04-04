import numpy as np
import pandas as pd
dict1={'class':[1,2,3,4,5],
       'marks':[45,34,56,78,23],
       'students':[24,25,23,27,23]}
df=pd.DataFrame(dict1)
print(df)
print(df.describe())
df.index=['first','second','third','fourth','fifth']
print(df)
df.loc['second','marks']=100
print(df)