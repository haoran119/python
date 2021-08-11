# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets


# In[2]:


"""
手写体数字，监督学习
1、样本集：一批手写体数字的图片，带标签（0-9），10类
样本数据量为1797，存在sklearn的datasets里。
每一个数据样本都是由image, target两部分组成。
image是一个尺寸为8*8的图像（手写的数字0-9），
target是图像的类别（数字0-9）。
2、划分训练集和测试集
3、选一个算法，构建模型，KNN
4、训练模型
5、预测、验证
6、模型优化（SVM, 决策树）
7、保存模型（.model, load, predict）
8、新建多张手写体图片，让模型来识别新的图片
"""
sample_data = datasets.load_digits()
images = sample_data.data
labels = sample_data.target


# In[3]:


#划分训练集和测试集
train_data, test_data, train_labels, test_labels = train_test_split(images, labels, test_size=0.1)


# In[4]:


#选择模型
model_knn = KNeighborsClassifier(n_neighbors=4, algorithm='auto', weights='distance')


# In[5]:


#训练模型
model_knn.fit(train_data, train_labels)
#KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#           metric_params=None, n_jobs=1, n_neighbors=4, p=2,
#           weights='distance')

# In[6]:


#预测、验证
pred = model_knn.predict(test_data)
print("pred : \n", pred)
print("test_labels : \n", test_labels)
#pred : 
# [3 4 1 4 4 0 0 8 2 9 8 9 6 1 3 3 7 8 5 1 3 2 1 2 7 4 8 5 7 1 0 2 4 0 7 3 1
# 5 3 4 6 2 5 1 6 3 4 5 4 9 3 6 5 0 0 4 5 2 0 7 7 6 5 1 2 9 9 2 7 6 3 2 3 8
# 6 7 6 4 0 2 2 8 8 8 5 0 2 0 4 2 2 0 6 6 6 0 9 8 9 5 3 8 5 7 9 6 3 0 3 9 5
# 1 0 9 6 7 0 1 5 3 0 3 4 9 2 3 8 2 2 5 7 2 6 2 7 3 1 4 5 9 9 6 6 9 7 1 3 7
# 1 9 8 6 9 9 6 5 0 5 6 9 7 7 5 0 3 8 5 9 2 0 9 3 1 2 9 3 7 6 9 6]
#test_labels : 
# [3 4 1 4 4 0 0 8 2 9 8 9 6 1 3 3 7 8 5 1 3 2 1 2 7 4 8 5 7 1 0 2 4 0 7 3 1
# 5 3 4 6 2 5 1 6 3 4 5 4 9 3 6 5 0 0 4 5 2 0 7 7 6 5 1 2 9 9 2 7 6 3 2 3 8
# 6 7 6 4 0 2 2 8 8 8 5 0 2 0 4 2 2 0 6 6 6 0 9 8 7 5 3 8 5 7 9 6 3 0 3 9 5
# 1 0 9 6 7 0 1 5 3 0 3 4 9 2 3 8 2 2 5 7 2 6 2 7 3 1 4 5 9 9 6 6 9 7 1 3 7
# 1 9 8 6 9 9 6 5 0 5 6 9 7 7 5 0 3 8 5 9 2 0 9 3 1 2 9 3 7 6 9 6]

# In[7]:


#查看准确率
acc = accuracy_score(pred, test_labels)
print("Accuracy rate : %.3f" % acc)
#Accuracy rate : 0.994

