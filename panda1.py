#pd.DataFrame(dictionary)-arranges the elements in the form of excel sheet
#variable.describe()-gives the statistical analysis of the numerical part
#variable.index to change the index of the sheet
#variable.to_csv('any name for the file')
#pd.read_csv('file name')- to read the csv file
#variable.loc[row,column]- to modify the value at that position
#variable.drop(index, axis=0/1)- to delete the row or column
#variable.iloc(row,column)- to get the value of a particular cell
#variable.reset_index(drop=True)- to reset the indexing
#variable.drop_duplicates(arguement)- remove duplicate values







import numpy as np
import pandas as pd
dict1= {'name':['raj','shiv','yash','harsh'],
        'marks':[100,28,67,23],
        'city':['lucknow','dhampur','bareilly','muzzafarnagar']}
df= pd.DataFrame(dict1)
print(df)
print()