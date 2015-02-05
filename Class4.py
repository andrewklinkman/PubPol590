from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590/Data"
git_dir = "/Users/andrewklinkman/GitHub/PubPol590"
csv_file1 = "/small_data_w_missing_duplicated.csv"
csv_file2 = "/sample_assignments.csv"

###IMPORT DATA
df1 = pd.read_csv(main_dir+csv_file1, na_values = ['-', 'NA'])
df2 = pd.read_csv(main_dir+csv_file2, na_values = ['-', 'NA'])

##CLEAN DATA
#DF1
df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(subset = ['panid', 'date'], take_last = True)

#DF2
df2 = df2[['panid', 'group']]

#nothing telling who is in what group in df1

#COPY DATAFRAMES -----------------------
df3 = df2 #creating a reference (change df2 = change df3)
df4 = df2.copy() #creating a copy (at that exact moment in time)
#python is a reference language...


#REPLACING DATA---------------------
df2.group = df2.group.replace(['T', 'C'], [1,0]) #arg 1 = find...arg 2 = replace
df2.group.replace(['T', 'C'], [1,0])

df3 #now df3 changes


#MERGING --------------------
pd.merge(df1, df2) #attach df2 to df1...order matters. maybe. Default = many-to-one merge using the
#intersection between the two. automatically finds keys it has in common. panid exists in both.

pd.merge(df1, df2, on = ['panid'], how = 'inner') #inner = default
pd.merge(df1, df2, on = ['panid'], how = 'outer') #cartesian product (errythang that's in either of them)

df5 = pd.merge(df1, df2, on = ['panid'], how = 'inner')

#ROW BINDS AND COLUMN BINDS ---------------
df2
df4

#row bind
pd.concat([df2, df4]) #default = rowbind (stack)

pd.concat([df2, df4], axis = 0) #def
pd.concat([df2, df4], axis = 0, ignore_index = True) #if you don't ignore, the indices from the originals will be kept
pd.concat([df2, df4], axis = 1) #column bind

