# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


# 1. 线形图 y = ax + b
x = np.linspace(1, 21, 20)
y = 2 * x + 3
y2 = np.sin(x)

plt.plot(x, y, 'm^:', x, y2)

plt.show()


# In[3]:


# 2. 散点图
n = 1024
x = np.random.normal(0, 1, n) #1024个符合高斯分布的值
y = np.random.normal(0, 1, n)

plt.scatter(x, y, s=np.random.rand(n)*50, c=np.random.rand(n), alpha=0.7)

plt.show()


# In[4]:


# 3. 柱状图
n = 10
x = np.arange(n)
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(x, y1, facecolor='red', edgecolor='white')
plt.bar(x, -y2, facecolor='blue', edgecolor='black')

for xx, y in zip(x, y1):
    plt.text(xx, y + 0.1, '%0.2f'%y, ha='center', va='bottom')

for xx, y in zip(x, -y2):
    plt.text(xx, y - 0.1, '%0.2f'%y, ha='center', va='bottom')

plt.ylim(-1.5, 1.5)

plt.show()


# In[5]:


# 4. 3D
fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

x, y = np.meshgrid(x, y)
#[[-4.   -3.75 -3.5  ...  3.25  3.5   3.75]
# [-4.   -3.75 -3.5  ...  3.25  3.5   3.75]
# [-4.   -3.75 -3.5  ...  3.25  3.5   3.75]
# ...
# [-4.   -3.75 -3.5  ...  3.25  3.5   3.75]
# [-4.   -3.75 -3.5  ...  3.25  3.5   3.75]
# [-4.   -3.75 -3.5  ...  3.25  3.5   3.75]]
print(x)
#[[-4.   -4.   -4.   ... -4.   -4.   -4.  ]
# [-3.75 -3.75 -3.75 ... -3.75 -3.75 -3.75]
# [-3.5  -3.5  -3.5  ... -3.5  -3.5  -3.5 ]
# ...
# [ 3.25  3.25  3.25 ...  3.25  3.25  3.25]
# [ 3.5   3.5   3.5  ...  3.5   3.5   3.5 ]
# [ 3.75  3.75  3.75 ...  3.75  3.75  3.75]]
print(y)

z = np.sin(np.sqrt(x**2 + y**2))

ax.plot_surface(x, y, z, cmap=plt.get_cmap('autumn'))

plt.show()


# In[6]:


# 5. 一图多画
x = np.linspace(0, 5, 5)
y1 = x**2
y2 = 2 * x
y3 = np.sin(x)
y4 = np.cos(x)

ax1 = plt.subplot(221)
plt.plot(x, y1)
ax2 = plt.subplot(2, 2, 2)
plt.plot(x, y2)
ax3 = plt.subplot(223)
plt.plot(x, y3)
ax4 = plt.subplot(2, 2, 4)
#plt.plot(x, y4)

plt.show()

