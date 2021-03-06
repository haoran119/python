# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.DataFrame(pd.read_excel('originalData.xlsx'))

#         date   hour  pressure  wind_direction  temperature
#0  2016-07-01    0.0    1000.4           225.0         26.4
#1  2016-07-01    NaN       NaN             NaN          NaN
#2  2016-07-01    6.0     998.9           212.0         31.7
#3  2016-07-01  235.0     998.7           244.0          NaN
#4  2016-07-01   12.0     999.7           222.0          NaN
#5  2016-07-01   15.0    1000.0           102.0          NaN
#6  2016-07-01    NaN     998.8           202.0         26.0
#7  2016-07-01    NaN    1000.2           334.0         25.5
#8  2016-07-01    NaN    1000.2           334.0         25.5
#9  2016-07-02    3.0    1002.4            46.0         30.0
#10 2016-07-02    6.0    1001.3            37.0         29.3
#11 2016-07-02    9.0    1001.9           345.0         25.9
#12 2016-07-02   12.0    1003.6           113.0         25.1
#13 2016-07-02   12.0    1003.6           113.0         25.1
#14 2016-07-02   15.0    1002.4           138.0         25.3
#             hour     pressure  wind_direction  temperature
#count   11.000000    14.000000       14.000000    11.000000
#mean    29.545455  1000.864286      190.500000    26.890909
#std     68.313049     1.685963      102.932951     2.311473
#min      0.000000   998.700000       37.000000    25.100000
#25%      6.000000   999.775000      113.000000    25.400000
#50%     12.000000  1000.300000      207.000000    25.900000
#75%     13.500000  1002.275000      239.250000    27.850000
#max    235.000000  1003.600000      345.000000    31.700000
print(data)
print(data.describe())


# In[3]:

#RangeIndex(start=0, stop=15, step=1)
#Index(['date', 'hour', 'pressure', 'wind_direction', 'temperature'], dtype='object')
print(data.index)
print(data.columns)


# In[4]:

#        date   hour  pressure  wind_direction  temperature
#0 2016-07-01    0.0    1000.4           225.0         26.4
#1 2016-07-01    NaN       NaN             NaN          NaN
#2 2016-07-01    6.0     998.9           212.0         31.7
#3 2016-07-01  235.0     998.7           244.0          NaN
#4 2016-07-01   12.0     999.7           222.0          NaN
#5 2016-07-01   15.0    1000.0           102.0          NaN
#         date  hour  pressure  wind_direction  temperature
#9  2016-07-02   3.0    1002.4            46.0         30.0
#10 2016-07-02   6.0    1001.3            37.0         29.3
#11 2016-07-02   9.0    1001.9           345.0         25.9
#12 2016-07-02  12.0    1003.6           113.0         25.1
#13 2016-07-02  12.0    1003.6           113.0         25.1
#14 2016-07-02  15.0    1002.4           138.0         25.3
print(data.head(6))
print(data.tail(6))


# In[5]:


# 1. ?????????????????????3??????
data.dropna(axis=0, thresh=3, inplace=True)
data.reset_index(drop=True, inplace=True)

#         date   hour  pressure  wind_direction  temperature
#0  2016-07-01    0.0    1000.4           225.0         26.4
#1  2016-07-01    6.0     998.9           212.0         31.7
#2  2016-07-01  235.0     998.7           244.0          NaN
#3  2016-07-01   12.0     999.7           222.0          NaN
#4  2016-07-01   15.0    1000.0           102.0          NaN
#5  2016-07-01    NaN     998.8           202.0         26.0
#6  2016-07-01    NaN    1000.2           334.0         25.5
#7  2016-07-01    NaN    1000.2           334.0         25.5
#8  2016-07-02    3.0    1002.4            46.0         30.0
#9  2016-07-02    6.0    1001.3            37.0         29.3
#10 2016-07-02    9.0    1001.9           345.0         25.9
#11 2016-07-02   12.0    1003.6           113.0         25.1
#12 2016-07-02   12.0    1003.6           113.0         25.1
#13 2016-07-02   15.0    1002.4           138.0         25.3
print(data)


# In[6]:


# 2. ???????????????hour??????10???temperature??????25.5
data.fillna({'hour':10, 'temperature':25.5}, inplace=True)

#         date   hour  pressure  wind_direction  temperature
#0  2016-07-01    0.0    1000.4           225.0         26.4
#1  2016-07-01    6.0     998.9           212.0         31.7
#2  2016-07-01  235.0     998.7           244.0         25.5
#3  2016-07-01   12.0     999.7           222.0         25.5
#4  2016-07-01   15.0    1000.0           102.0         25.5
#5  2016-07-01   10.0     998.8           202.0         26.0
#6  2016-07-01   10.0    1000.2           334.0         25.5
#7  2016-07-01   10.0    1000.2           334.0         25.5
#8  2016-07-02    3.0    1002.4            46.0         30.0
#9  2016-07-02    6.0    1001.3            37.0         29.3
#10 2016-07-02    9.0    1001.9           345.0         25.9
#11 2016-07-02   12.0    1003.6           113.0         25.1
#12 2016-07-02   12.0    1003.6           113.0         25.1
#13 2016-07-02   15.0    1002.4           138.0         25.3
print(data)


# In[7]:


# 3. ??????hour>24??????
num = data.index.max()

for i in range(num):
    if data.loc[i, 'hour'] > 24:
        data.drop([i], inplace=True)
        print('hour > 24, deleted')
        
data.reset_index(drop=True, inplace=True)        

#hour > 24, deleted
#         date  hour  pressure  wind_direction  temperature
#0  2016-07-01   0.0    1000.4           225.0         26.4
#1  2016-07-01   6.0     998.9           212.0         31.7
#2  2016-07-01  12.0     999.7           222.0         25.5
#3  2016-07-01  15.0    1000.0           102.0         25.5
#4  2016-07-01  10.0     998.8           202.0         26.0
#5  2016-07-01  10.0    1000.2           334.0         25.5
#6  2016-07-01  10.0    1000.2           334.0         25.5
#7  2016-07-02   3.0    1002.4            46.0         30.0
#8  2016-07-02   6.0    1001.3            37.0         29.3
#9  2016-07-02   9.0    1001.9           345.0         25.9
#10 2016-07-02  12.0    1003.6           113.0         25.1
#11 2016-07-02  12.0    1003.6           113.0         25.1
#12 2016-07-02  15.0    1002.4           138.0         25.3
print(data)


# In[8]:


# 4. ?????????????????????????????????????????????????????????????????????????????????????????????
data.drop_duplicates(keep='first', inplace=True)
data.reset_index(drop=True, inplace=True)

#         date  hour  pressure  wind_direction  temperature
#0  2016-07-01   0.0    1000.4           225.0         26.4
#1  2016-07-01   6.0     998.9           212.0         31.7
#2  2016-07-01  12.0     999.7           222.0         25.5
#3  2016-07-01  15.0    1000.0           102.0         25.5
#4  2016-07-01  10.0     998.8           202.0         26.0
#5  2016-07-01  10.0    1000.2           334.0         25.5
#6  2016-07-02   3.0    1002.4            46.0         30.0
#7  2016-07-02   6.0    1001.3            37.0         29.3
#8  2016-07-02   9.0    1001.9           345.0         25.9
#9  2016-07-02  12.0    1003.6           113.0         25.1
#10 2016-07-02  15.0    1002.4           138.0         25.3
print(data)


# In[9]:


# 5. ????????????
randnum = np.random.permutation(data.index.size)

#[ 4  0 10  3  1  5  8  9  7  2  6]
print(randnum)


# In[10]:


data2 = data.take(randnum)

#         date  hour  pressure  wind_direction  temperature
#4  2016-07-01  10.0     998.8           202.0         26.0
#0  2016-07-01   0.0    1000.4           225.0         26.4
#10 2016-07-02  15.0    1002.4           138.0         25.3
#3  2016-07-01  15.0    1000.0           102.0         25.5
#1  2016-07-01   6.0     998.9           212.0         31.7
#5  2016-07-01  10.0    1000.2           334.0         25.5
#8  2016-07-02   9.0    1001.9           345.0         25.9
#9  2016-07-02  12.0    1003.6           113.0         25.1
#7  2016-07-02   6.0    1001.3            37.0         29.3
#2  2016-07-01  12.0     999.7           222.0         25.5
#6  2016-07-02   3.0    1002.4            46.0         30.0
print(data2)


# In[11]:


# 6. ????????????
data3 = data.sample(8)

#        date  hour  pressure  wind_direction  temperature
#4 2016-07-01  10.0     998.8           202.0         26.0
#0 2016-07-01   0.0    1000.4           225.0         26.4
#2 2016-07-01  12.0     999.7           222.0         25.5
#1 2016-07-01   6.0     998.9           212.0         31.7
#5 2016-07-01  10.0    1000.2           334.0         25.5
#9 2016-07-02  12.0    1003.6           113.0         25.1
#7 2016-07-02   6.0    1001.3            37.0         29.3
#8 2016-07-02   9.0    1001.9           345.0         25.9
print(data3)
data3.to_csv('data3.csv')