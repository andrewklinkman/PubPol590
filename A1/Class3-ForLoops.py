from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os #how to correctly import file paths

#Class 3 - 1.28.15

#main dir = where the data goes
main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590/Data"

#git dir = where the code goes
git_dir = "/Users/andrewklinkman/GitHub/PubPol590/"

csv_file = "sample_data_clean.csv"

#FOR LOOPS --------------------------------------------
df = pd.read_csv(os.path.join(main_dir, csv_file))

list1 = range(10,15)
list2 = ['a', 'b', 'c']
list3 = [1, 'a', True]

#iterating over elements (for loops)
for v in list2:
    v
    print(v)
    
for v in list3:
    print v,' ', type(v)
    

list4 = []
for v in list1:
    v2 = v**2
    list4.append(v2)
    
list4

[v**2 for v in list1] #shorthand way to use for loops. whatever comes out of here is gonna be a list

list6 = [v**2 < 144 for v in list1]
list6


#iterating using enumerate
list7 = [ [i, float(v)/2] for i, v in enumerate(list1)] #enumerate pairs index with value
list7

#iterate through series
[v>2 for v in df['consump']]

[[i,v] for i,v in df['consump'].iteritems()] #like enumerate, but returns the actual index value (not just the #)

#iterate through a dataframe
[v for v in df]
[df[v] for v in df]
[[i,v] for i, v in df.iteritems()]


