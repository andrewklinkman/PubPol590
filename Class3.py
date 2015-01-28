from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os #how to correctly import file paths

#Class 3 - 1.28.15

#main dir = where the data goes
main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590/Data"

#git dir = where the code goes
git_dir = "/Users/andrewklinkman/GitHub/PubPol590/"

csv_file_good = "sample_data_clean.csv"
csv_file_bad = "/sample_data_clean.csv"

#OS MODULE-------------------
df = pd.read_csv(os.path.join(main_dir, csv_file_good))
df = pd.read_csv(main_dir+csv_file_good)

#PYTHON DATA TYPES-------------

#strings
str1 = "hello, computer" #double and single quotes ok
str2 = 'hello, human'
str3 = u'eep' #unicode = all computers can understand this text. universal.

type(str1)
type(str2)
type(str3)

#numeric types
int1 = 10
float1 = 20.56
long1 = 17529840912985000000000000000000999999

#logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1) # 0 = false



#CREATING LISTS AND TUPLES-------------------

#in brief, lists can be changed and tuples cannot. we will almost exclusively use lists
list1 = []
list2 = [1,2,3]
list2[2] #index starting at 0

list2[2] = 100

tup1=(8, 11, 29) #tuples have parenthesis
tup1[2]

#convert

list2 = list(tup1)
tup2 = tuple(list2)

#lists can be appended and extended
list2.append([3,[10,10]])
list2

list2 = [8, 3, 19]
list2.extend([3,6,8])
list2
len(list2)




#CONVERTING LISTS TO SERIES AND DATAFRAME---------------------
list4 = range(55,60)

list5 = range(95,100) #list from 0 to m-1

#list to series (series always have an index)
s1 = Series(list4)
s2 = Series(list5)

s1
s2

#create dataframe from lists or series
    #only create with vectors of the same length
list7 = range(60, 65)
zip(list4, list5) #think zipper - makes tuples from the same index positions in each list
zip1 = zip(list4, list5, list7)
df1 = DataFrame(zip1)

df2 = DataFrame(zip1, columns = ['two', 'apple', ':)'])
df2[':)']
df2[['apple', ':)']][0:3] #get 1st, 2nd and 3rd rows of apple and :) columns

#make a dataframe using dict notation
df3 = DataFrame({':(':list4, 9:list5, ':0':list7})#curly brackets = create dictionary object, ordering = alphanumeric
df3


