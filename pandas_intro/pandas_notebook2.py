'''
pandas notebook part II
'''
# Environment Setup
import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss

# Data Loading and Saving
 # .txt .csv
data1_1 = pd.read_csv('demodata.csv')
data1_2 = pd.read_csv('demodata.csv', index_col = 'clientid')
# source: /Library/Python/2.7/site-packages/matplotlib/mpl-data/sample_data/demodata.csv

data2_1 = pd.read_fwf('loc_and_time3.txt')
data2_2 = pd.read_fwf('loc_and_time3.txt', header = None)
data2_3 = pd.read_fwf('loc_and_time3.txt', names = ['time', 'Area_Code', 'CellID'])
data2_4 = pd.read_fwf('loc_and_time3.txt', names = ['time', 'Area_Code', 'CellID'], index_col = 'time')
# source : http://realitycommons.media.mit.edu/realitymining.html

data3 = pd.read_csv('311-service-requests.csv', nrows = 100000, parse_dates = ['Created Date']) 

# source : http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/NYC%20Python%20talk.ipynb

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
data4 = pd.DataFrame(records)

# source: http://www.usa.gov/About/developer-resources/1usagov.shtml


# Data Writing out to .txt
df6.to_csv('people.csv')
df6.to_csv('people2.csv', sep = '|')
df6.to_csv('people3.csv', index = False, header = False) 
