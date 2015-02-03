from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590/Data"
git_dir = "/Users/andrewklinkman/GitHub/PubPol590/A2"
csv_file = "/small_data_w_missing_duplicated.csv"

#import csv...first cut
csv1 = pd.read_csv(main_dir+csv_file)
csv1

#for all types of potentially missing symbols
missing = ['.', 'NA', 'NULL', '', '-']

#import again, with nas
csv1 = pd.read_csv(main_dir+csv_file, na_values = missing)
csv1

#vector of all the NaNs in consump column, just for fun
csvCons = csv1['consump'].isnull()

#drop all the second time duplicated rows
csv2 = csv1[csv1.duplicated()==False]
csv2 = csv1.drop_duplicates()

#find all rows where consump is null
csvCons = csv2['consump'].isnull()

#find duplicates based on panid and date
t_b = csv2.duplicated(subset = ['panid', 'date'])
b_t = csv2.duplicated(subset = ['panid', 'date'], take_last = True)
duplicates = (t_b | b_t)

#drop all rows where the first two columns are duplicated and the consump is Nan
dupMissing = (csvCons & duplicates)
csv3 = csv2[~dupMissing]

#average of remaining consump values
avgConsump = csv3['consump'].mean()

#still have null values in the data...is that ok?
csv3[csv3['consump'].isnull()]