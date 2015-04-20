from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

main_dir = "/Users/andrewklinkman/GitHub/PubPol590/A4/"

#change working dir
os.chdir(main_dir)

from logit_functions import *

do_logit??


#--------------------------SECTION 0---------------------------------------
#IMPORT DATA -------
df = pd.read_csv(main_dir+ '14_B3_EE_w_dummies.csv')
df= df.dropna(axis = 0, how='any')

#GET TARIFFS-------------
tariffs = [v for v in pd.unique(df['tariff']) if v!= 'E']
stimuli = [v for v in pd.unique(df['stimulus']) if v!= 'E']
tariffs.sort()
stimuli.sort()

#RUN LOGIT --------------
drop = [v for v in df.columns if v.startswith("kwh_2010")]
df_pretrial = df.drop(drop, axis = 1)

for i in tariffs:
    for j in stimuli:
        #dummy vars must start with "D_" and comsumption vars with "kwh_"
        #mc = True means remove multicollinear vals
        logit_results, df_logit = do_logit(df_pretrial, i, j, add_D = None, mc = False)

# QUICK MEANS COMPARISON WITH T-TEST BY HAND----------------
#create means
df_mean = df_logit.groupby('tariff').mean().transpose()
df_mean.B-df_mean.E

#do a t-test "by hand"
df_s=df_logit.groupby('tariff').std().transpose()
df_n=df_logit.groupby('tariff').count().transpose().mean()
top = df_mean['B']-df_mean['E']
bottom = np.sqrt(df_s['B']**2/df_n['B']+df_s['E']**2/df_n['E'])

tstats = top/bottom
sig = tstats[np.abs(tstats)>2]
sig.name = 't-stats'

#--------------------------SECTION 1---------------------------------------
#IMPORT DATA -------
df = pd.read_csv(main_dir+ 'task_4_kdfwh_w_dummies_wide.csv')
df= df.dropna(axis = 0, how='any')

#GET TARIFFS-------------
tariffs = [v for v in pd.unique(df['tariff']) if v!= 'E']
stimuli = [v for v in pd.unique(df['stimulus']) if v!= 'E']
tariffs.sort()
stimuli.sort()

#RUN LOGIT --------------
drop = [v for v in df.columns if v.startswith("kwh_2010")]
df_pretrial = df.drop(drop, axis = 1)

for i in tariffs:
    for j in stimuli:
        #dummy vars must start with "D_" and comsumption vars with "kwh_"
        #mc = True means remove multicollinear vals
        logit_results, df_logit = do_logit(df_pretrial, i, j, add_D = None, mc = False)

# QUICK MEANS COMPARISON WITH T-TEST BY HAND----------------
#create means
df_mean = df_logit.groupby('tariff').mean().transpose()
df_mean.C-df_mean.E

#do a t-test "by hand"
df_s=df_logit.groupby('tariff').std().transpose()
df_n=df_logit.groupby('tariff').count().transpose().mean()
top = df_mean['C']-df_mean['E']
bottom = np.sqrt(df_s['C']**2/df_n['C']+df_s['E']**2/df_n['E'])

tstats = top/bottom
sig = tstats[np.abs(tstats)>2]
sig.name = 't-stats'

sig
print(logit_results.summary())


#--------------------------SECTION 2---------------------------------------
df_logit['p_val'] = logit_results.predict()

df_logit['trt'] = 0 + (df_logit['tariff'] == 'C')
df_logit['w'] = np.sqrt(df_logit['trt']/df_logit['p_val']+(1-df_logit['trt'])/(1-df_logit['p_val']))

df_w = df_logit[['ID', 'trt', 'w']]


#--------------------------SECTION 3---------------------------------------
from fe_functions import *

#read file
df_long = pd.read_csv(main_dir+ 'task_4_kwh_long.csv')

#merge with df_logit
df = pd.merge(df_long, df_logit)

#create vars
df['TP'] = 0 + ((df.trial==1) & (df.trt==1))
df['log_kwh'] = (df['kwh'] + 1).apply(np.log)
df['mo_str'] = np.array(["0" + str(v) if v < 10 else str(v) for v in df['month']])
df['ym'] = df['year'].apply(str) + "_" + df['mo_str']

#set up regression vars
y = df['log_kwh']
P = df['trial']
TP = df['TP']
w = df['w']
mu = pd.get_dummies(df['ym'], prefix = 'ym').iloc[:, 1:-1]

#create new df
X = pd.concat([TP, P, mu], axis = 1)

#demean x and y
ids = df.ID
y = demean(y, ids)
x = demean(x, ids)

#RUN FIXED EFFECTS (CODE TAKEN FROM DAN)
## WITHOUT WEIGHTS
fe_model = sm.OLS(y, X) # linearly prob model
fe_results = fe_model.fit() # get the fitted values
print(fe_results.summary()) # print pretty results (no results given lack of obs)

# WITH WEIGHTS
## apply weights to data
yw = y*w # weight each y
nms = X.columns.values # save column names
Xw = np.array([x*w for k, x in X.iteritems()]) # weight each X value
Xw = Xw.T # transpose (necessary as arrays create "row" vectors, not column)
Xw = DataFrame(Xw, columns = nms) # update to dataframe; use original names

fe_w_model = sm.OLS(yw, Xw) # linearly prob model
fe_w_results = fe_w_model.fit() # get the fitted values
print(fe_w_results.summary()) # print pretty results (no results given lack of obs)