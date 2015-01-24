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
list(tgtData)