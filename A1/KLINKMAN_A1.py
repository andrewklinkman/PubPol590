from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#file paths
main_dir = "/Users/andrewklinkman/GitHub/PubPol590"
txt_file = "/A1/File1_small.txt"

#import data
tgtData = pd.read_table(main_dir + txt_file, " ")

#slice it up
rowSlice = tgtData[60:100]

#just the high stuff
highConsump = tgtData[tgtData.kwh > 30]

#check results
rowSlice
highConsump
len(rowSlice)
len(highConsump)