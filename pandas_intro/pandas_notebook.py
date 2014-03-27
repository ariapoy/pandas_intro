'''
This Document is notebook for the pandas
'''
# Environment setup
import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

# Data Structure in pandas
# Series = {list, dict} -> {Series}
v1 = [1,3,-5,-7,9]
v2 = [rd.randint(-3,4) for x in xrange(10)]
dt1 = {'Taipei': 9894.52, 'New Taipei': 1927.27, 'Taichung': 1220.86, 'Kaohsiung': 943.02, 'Tainan': 859.18}
# ref: http://en.wikipedia.org/wiki/List_of_Republic_of_China_administrative_divisions_by_population_density
 # Series
ser1 = pd.Series(v1)
ser2 = pd.Series(v2)
ser3 = pd.Series(dt1)

 # values
print ser1.values
print ser1[ser1 > 0] 
print ser1[1:3]
print ser1[[1,3,5]]
print pd.isnull(ser1)

 # index
idx1 = ['Taipei', 'New Taipei', 'Kaohsiung', 'Yilan']
ser4 = pd.Series(dt1, idx1)
print ser1.index 
print 2 in ser1
print pd.isnull(ser4)

 # operations
ser5 = ser1 + ser2
ser6 = ser3 + ser4
ser7 = ser1 + ser3

 # name or title of Series and index
ser3.name = 'density of population'
ser3.index.name = 'city'

# DataFrame {2D ndarry, dict of ..., list of ...} -> {DataFrame}
data1 = np.random.rand(4,3)
data2 = {'city': idx1, 'population': [2688140, 3955777, 2779790, 458378]}
data3 = {idx1[0]: {201401: 2688140, 201402: 2689327}, idx1[1]: {201401: 3955777, 201402: 3955842}, idx1[2]: {201401: 2779790, 201402: 2779653}, idx1[3]: {201401: 458378}}
# ref: http://sowf.moi.gov.tw/stat/month/list.htm
ser8 = df6[201401]

 # DataFrame
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df6 = pd.DataFrame(data3)
print type(df3)
print type(df3.city)
df8 = pd.DataFrame({ser3, ser8}) #error
df8 = pd.DataFrame([ser3, ser8]).T

 # values
print df2['city']
print df2.city
print df2.ix[2]
print df2.ix[[2,4]]
print df2['population']
df2['zscore_population'] = (df2['population'] - df2['population'].mean()) / df2['population'].std()
print df2
df2['degree of population'] = df2.population > df2['population'].mean() + df2['population'].std()
print df2
print df8.values
print df2.values

 # index and columns
df3 = pd.DataFrame(data2, columns = ['population', 'city'])
df4 = pd.DataFrame(data2, columns = ['city', 'population', 'density of population'])
df5 = pd.DataFrame(data2, columns = ['city', 'population'], index = ['one', 'two', 'three', 'four'])
print df3.columns
df2.rename(columns={'degree of population': 'high population'})
print df2
df7 = pd.DataFrame(data3, index = range(201401,201404))
print df7
print df6.201401 # error
print df6[201401]

# manage your data
df2.drop(['density of population'], axis = 1)
print df2
df6 = df6.T
print df6
 # reindex
idx3 = idx2.tolist()
idx3.append('Yilan')
idx3 = pd.Index(idx3)
print idx3
ser9 = ser3.reindex(idx3) # method = ffill or bfill
col1 = df6.columns.tolist()
col1.append(2)
df9 = df6.reindex(columns = col1)
 # drop (delete)
df9 = df9.drop(2, 1) # object and axis
df9 = df9.drop(['Taipei', 'New Taipei'])
 # filtering, editing
print ser4['New Taipei': 'Kaohsiung']
print df2[df2['zscore_population'] > 0]
 # data alignment operation
# recall ser4 = ser1 + ser2
ser10 = ser1.add(ser2, fill_value = 0)
 # function and mapping
frame = pd.DataFrame(np.random.randn(4,3), columns = list('cde'), index = list('poyi'))
print frame.apply(lambda x: x.max() - x.min()) # vector (Series)
print frame.apply(lambda x: x.max() - x.min(), axis = 1)
print frame.applymap(lambda x: '%.3f' % x) # element
 # sorting and ranking
print frame.sort_index()
print frame.sort_index(axis = 1, ascending = False) # reverse
print frame.c.order() # Series function
print frame.sort_index(by= 'e')
print frame.rank()
print frame.rand(axis = 1) # method = min, max, first
 # duplicate index or value
series = pd.Series(['c','a','d','a','a','b','b','c','c','a'])
print series.unique()
print series.value_counts()
print series[series.isin(['b'])]

#####
# Descirptive Statistics
 # DataFrame: count, describe, min, max, idxmin, idxmax, ?quantile, sum, min, max, median, mad, var, std, skew(3rd moment), kurt(4th moment), cumsum, cummin/cummax, cumprod, diff/pct_change, cov, corr

 # Series: argmin, argmax

# Missing value
ser5.fillna(0, inplace = True)
print ser5
df8.fillna({'density of population': df8.mean()[0], 201401: df8.mean()[1]})
print df8
####

# Index
idx1 = pd.Index(range(5))
print idx1
idx2 = ser3.index
print idx2
print idx2[1]
idx2[1] = 'New Yilan' #error
# append, diff, intersection, union, delete or drop, insert, unique

####
# hierachical indexing
 # series
a = [1,2,3]*3
a.append(1)
data4 = pd.Series(np.random.randn(10), index = [list('aaabbbcccd'), a])
print data4.index
print data['b']
print data['b',1]
DATA4 = data4.unstack() # Series to DataFrame
print DATA4
# dataframe
data5 = pd.DataFrame(np.random.rand(4,3), index = [list('ppyy'), [1,2,1,2]], columns = [list('goo'), list('rgb')])
print data5

####
# Statistic for hierachical
data5.sum(level = 1, axis = 1) # use level and axis


####

