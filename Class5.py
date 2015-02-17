from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/andrewklinkman/Dropbox/Duke/School Stuff 14-15/Spring 2015/PUBPOL 590/Class 5/"

#PATHING
all_files = [os.path.join(main_dir, v) for v in os.listdir(main_dir) if v.startswith("file")]

#STACKING
df = pd.concat([pd.read_csv(v, names=['panid', 'date', 'kwh']) for v in all_files], ignore_index=True)

#MERGING
df_assign = pd.read_csv(main_dir + "sample_assignments.csv", usecols = [0,1])

df = pd.merge(df, df_assign)

#new stuff-----------------------------
#GROUPBY aka "Split, apply, combine"

grp1 = df.groupby(['assignment']) # .groupby objects for big data
gd1 = grp1.groups # CAUTION! don't do this with super big data. it will crash.

## peek inside gd1 (dictionary)
gd1.keys()
gd1['C'] # gd1 is a dict, so must use keys to get data
gd1.values()[0] # gd1.values() is a list, so we can use numerical indeces
gd1.viewvalues() # see all the values of the dictionary, gd1

## iteration properties of a dictionary
[v for v in gd1.itervalues()]
gd1.values() # equivalent to above

[k for k in gd1.iterkeys()]
gd1.keys() # equivalent

[(k,v) for k,v in gd1.iteritems()]
gd1

## split and apply (pooled data)
grp1['kwh'].mean()

## split and apply (panel/time series data)
grp2 = df.groupby(['assignment','date'])
gd2 = grp2.groups
gd2 # look at the dictionary (key, value) pairs
gd2[('T', '2-Jan')]
grp2['kwh'].mean() 

#TESTING FOR BALANCE-------------------------------
#(over time)
from scipy.stats import ttest_ind
from scipy.special import stdtr

#trying to construct two sets of data that we can compare
#example
a = [1, 4, 9, 2]
b = [1, 7, 8, 9]

t, p = ttest_ind(a, b, equal_var = False) #returns multiple values, can either assign to 
#two seperate vars, or to one tuple var
?ttest_ind

#set up data
grp = df.groupby(['assignment', 'date'])

trt = { k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0]=='T'}
ctrl = { k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0]=='C'}
#getting a set of all treatments by date
#grp.groups = dict.  .iteritems returns a key and a value pair. 
#each key is a tuple with two values
grp.groups.keys()[0][0] #first row, first position


#return new dictionary with key = second element of k
#and value = array of values
df.kwh[[30,60]] #returns a series
df.kwh[[30,60]].values #returns an array

#want to link up with date keys
keys = trt.keys()

#comparisons
diff = {k: (trt[k].mean()-ctrl[k].mean()) for k in keys}
tstats = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[0]) for k in keys}

pvals = {k: float(ttest_ind(trt[k], ctrl[k], equal_var = False)[1]) for k in keys}

t_p = {k: (tstats[k], pvals[k]) for k in keys}


##split by c/t, pooled w/o time
#groups1 = df.groupby(['assignment']) #splitting by 'assignment'
#groups1.groups #shows the groups, then the indices associated with each group
#
##apply the mean
#groups1['kwh'].apply(np.mean) #this is not an internal function to the groups object
#groups1['kwh'].mean() #this is an internal function (faster)
#
##magic functions! time it for 100 executions
#%timeit -n 1000 groups1['kwh'].apply(np.mean) #this is not an internal function to the groups object
#%timeit -n 1000 groups1['kwh'].mean() #this is an internal function (faster)
#
##type series. and hit tab
#
#
##split by c/t, pooled w/ time
#groups2 = df.groupby(['assignment', 'date']) #splitting by 'assignment'
#groups2.groups #shows the groups, then the indices associated with each group
#
##apply the mean
#groups2['kwh'].mean() #this is an internal function (faster)
#
#
##UNSTACK
#
#gp_mean = groups2['kwh'].mean()
#
#type(gp_mean)
#
#gp_unstack = gp_mean.unstack('assignment')
#
#gp_unstack['T']['1-Jan']