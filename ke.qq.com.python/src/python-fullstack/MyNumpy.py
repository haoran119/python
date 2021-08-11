# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# 创建数组

list1 = [ 1, 3, 5, -2, 0, -9 ]
list2 = [ 2, 4, -3, -7, 1, -7 ]
list3 = [ [2, 5, 0], [11, 3, 4] ]
list4 = [ [3, -1, 8], [9, -3, 9] ]


# In[3]:


arr1 = np.array( list1 )

#[ 1  3  5 -2  0 -9]
print(arr1)


# In[4]:


arr4 = np.array( list3 )

#[[ 2  5  0]
# [11  3  4]]
print(arr4)


# In[5]:


arr2 = np.arange( 1, 10, 2 )

#[1 3 5 7 9]
print(arr2)


# In[6]:


arr3 = np.linspace( 1, 10, 4 )

#[ 1.  4.  7. 10.]
print(arr3)


# In[7]:


arr_zero = np.zeros( (3, 4)) # zeros参数是元组()

#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
print(arr_zero)


# In[8]:


arr_one = np.ones( (3, 3) )

#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
#[[100. 100. 100.]
# [100. 100. 100.]
# [100. 100. 100.]]
print(arr_one)
print(arr_one * 100)


# In[9]:


arr_eye = np.eye( 4, 4 ) # 对角线上元素为1，其他为0

#[[1. 0. 0. 0.]
# [0. 1. 0. 0.]
# [0. 0. 1. 0.]
# [0. 0. 0. 1.]]
print(arr_eye)


# In[10]:


arr_eye2 = np.eye( 4, 5 )

#[[1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
# [0. 0. 1. 0. 0.]
# [0. 0. 0. 1. 0.]]
print(arr_eye2)


# In[11]:


# 数组的索引和切片

#[ 5 -2  0]
#[[3 4]]
print(arr1[2:5]) # 左闭右开
print(arr4[1:2, 1:3])


# In[12]:


# 通用的函数

#sqrt : 
# [[1.41421356 2.23606798 0.        ]
# [3.31662479 1.73205081 2.        ]]
#exp : 
# [[7.38905610e+00 1.48413159e+02 1.00000000e+00]
# [5.98741417e+04 2.00855369e+01 5.45981500e+01]]
print("sqrt : \n", np.sqrt(arr4))
print("exp : \n", np.exp(arr4))


# In[13]:


arr2 = np.array( list2 )
new_arr = np.maximum( arr1, arr2 )

#[ 2  4  5 -2  1 -7]
print(new_arr)


# In[14]:


# ReLU >0 保留原值，<0 取0
new_arr = np.maximum(0, arr1)

#[1 3 5 0 0 0]
print(new_arr)


# In[15]:

#(array([[0.41421356, 0.23606798, 0.        ],
#       [0.31662479, 0.73205081, 0.        ]]), array([[1., 2., 0.],
#       [3., 1., 2.]]))
print( np.modf( np.sqrt( arr4 ) ) ) # 把整数部分和小数部分，生成两个独立的数组


# In[16]:


new_arr1 = np.where( arr2>0, 'True', 'False' ) # if condition: x, y

#['True' 'True' 'False' 'False' 'True' 'False']
print(new_arr1)


# In[17]:

#[-7 -3  1  2  4]
#[ 0  2  3  4  5 11]
print( np.unique( arr2 ) )
print( np.unique( arr4 ) )


# In[18]:


# 数组作为文件来输入和输出

np.save( 'myarr', arr2 ) # 把数组保存为文件 .npy


# In[19]:


new_arr2 = np.load( 'myarr.npy' )

#[ 2  4 -3 -7  1 -7]
print(new_arr2)


# In[20]:


np.savez( 'myarrzip', a1=arr1, a2=arr2, a3=arr3 )
arr = np.load( 'myarrzip.npz' )

#[ 1  3  5 -2  0 -9]
print(arr['a1'])


# In[21]:


# 线性代数 矩阵
# 矩阵的合并

arr5 = np.array( list3 )
arr6 = np.array( list4 )

#[[ 2  5  0  3 -1  8]
# [11  3  4  9 -3  9]]
#[[ 2  5  0]
# [11  3  4]
# [ 3 -1  8]
# [ 9 -3  9]]
print( np.hstack( [arr5, arr6] ) )
print( np.vstack( [arr5, arr6] ) )


# In[22]:


# 点乘

arr6 = np.array( list4 ).reshape( 3, 2 ) 

#[[ 3 -1]
# [ 8  9]
# [-3  9]]
#[[ -5  12  -4]
# [115  67  36]
# [ 93  12  36]]
print( arr6 )
print( arr6.dot( arr5 ) )


# In[23]:

#[[ 3  8 -3]
# [-1  9  9]]
print( np.transpose(arr6) ) # 转置