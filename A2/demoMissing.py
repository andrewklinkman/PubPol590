from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#file paths
main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590"
git_dir = "/Users/andrewklinkman/GitHub/PubPol590/A2"
csv_dir = "/sample_missing.csv"

#IMPORTING DATA (setting missing values = sentinels)-------------------

df = pd.read_csv(git_dir + csv_dir)

df.head(10) #top 10 values - default = 5
df[:10]
df.tail(10)

df['consump'].head(10).apply(type) #apply function 'type' to all records

#we don't want string data. periods are common missing data placeholders in some languages
#so, we need to create new sentinels to adjust for this. na_values = use sentinels

missing = ['.', 'NA', 'NULL', '']#vector of potential missing symbols

df = pd.read_csv(git_dir + csv_dir, na_values = missing)

#NaN = not a number

df['consump'].head(10).apply(type)

#MISSING DATA (using smaller dataframe) -----------------------------
#quick tip: repeat lists by multiplication
[1,2,3] * 3 #makes a new list, repeating this list x times

#types of missing data:
None #standard
np.nan #from numpy

type(None)
type(np.nan) #missing value that is considered numeric

#create a small sample dataset
zip1 = zip([2,4,8], [np.nan, 5, 7], [np.nan, np.nan, 22])
df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])

#search for missing data using 
df1.isnull() #pandas method to find missing data

#FIND METHODS FOR ANY OBJ
#type object, period, then hit tab
df1.isnull() #pandas
np.isnan(df1) #numpy

#subset of columns
cols = ['a', 'c']
df1[cols].isnull() #.notnull = opposite

df1['b'].isnull() #creates a vector -> more useful

# FILLING IN/DROPPING MISSING VALUES ----------------------
#pandas method 'fillna'
df2 = df1.fillna(999)

#dropping = slightly more usual
df1.dropna() #drops ROWS with any missing values
df1.dropna(axis = 0, how = 'any') #drop rows with any missing values
df1.dropna(axis = 1, how = 'any') #drop cols
df1.dropna(axis = 0, how = 'all') #only drop where whole row is empty

df.dropna(axis = 0, how = 'all')

#SEEING ROWS WITH MISSING DATA --------------------------
df3 = df.dropna(how = 'all')
df3.head(10)
rows = df3['consump'].isnull()
df3[rows]



