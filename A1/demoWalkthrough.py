from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/andrewklinkman/GitHub/PubPol590"
csv_file = "/A1/sample_data_clean.csv"
txt_file = "/A1/sample_data_clean.txt"

main_dir + csv_file
main_dir + txt_file

#read_csv and read_table
#table = more general table (default = tab)




txt_file2 = "/A1/File1_small.txt"

tgtData = pd.read_table(main_dir + txt_file2, " ")

#check type
type(tgtData)
type(main_dir)

#exploring dataframe
list(tgtData) #get names

#how to look at the data...
#way1 - extracting data
m = tgtData.meterid
#way2 - dictlike key
m2 = tgtData['meterid']

type(m2)

##boolean operators
#compare any two objects OF SAME TYPE
#==, not =
m == m2
m >= m2

#other operators <, !=, <=

#row extraction
#way1 - row slicing
tgtData[60:90] #doesn't include 90
tgtData[0:10]
tgtData[:10] #index starts at 0 in python

tgtData[0:10] == tgtData[:10]
#no single digits
tgtData[10:11]

#can also do it with columns/series
m[9:100] #with individual vars
tgtData.meterid[9:100] ==m[9:100]

#way2 - extraction by boolean indexing
#
tgtData[tgtData.meterid== 1392]


list(tgtData)
tgtData.kwh
len(tgtData[tgtData.kwh >=1])




