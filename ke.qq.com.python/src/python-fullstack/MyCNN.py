# coding: utf-8

# In[1]:


"""
基于CNN的手写体数字识别

迭代一轮 80s
"""
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K


# In[2]:


# 设置初始参数
batch_size = 128 # 一批喂给模型多少张图片 60000
num_classes = 10 # 分类 0 - 9
epochs = 12 # 迭代次数

img_rows, img_cols = 28, 28 # 28 * 28


# In[3]:


# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data() # 加载数据集，第一次运行慢

# 判断backend theano, tensorflow
# 彩色图片 RGB 3 通道，灰度图 1 通道
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols) # (60000, 1, 28, 28)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    intput_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0],  img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)


# In[4]:


# 数据处理

# image处理
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#x_train shape:  (60000, 28, 28, 1)
#60000 train samples
#10000 test samples
print('x_train shape: ', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# labels处理
# 5 -> [0000010000] 2 -> [0010000000]
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# In[5]:


# 1. 选择模型 
model = Sequential() # 序贯模型


# In[6]:


# 2. 构建网络层
# CNN的参数 权重（卷积核的构成），卷积核大小，数量，池化大小，步长，dropout rate
model.add(Conv2D(32,
                 kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape)) # 卷积层1

model.add(Conv2D(64,
                 (3, 3),
                 activation='relu')) # 卷积层2

model.add(MaxPooling2D(pool_size=(2, 2))) # 池化, 默认步长1

model.add(Dropout(0.25)) # 防止过拟合：训练集特征提取太细致，不适用于测试集

model.add(Flatten()) # 压平

model.add(Dense(128,
                activation='relu')) # 全连接：所有神经元之间都是互相连接的

model.add(Dropout(0.5)) # 扔掉50%

model.add(Dense(num_classes,
                activation='softmax')) # 全连接，多分类


# In[7]:


# 3. 编译
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


# In[8]:


# 4. 训练
model.fit(x_train,
          y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test)) # 开始训练

#Train on 60000 samples, validate on 10000 samples
#Epoch 1/12
#60000/60000 [==============================] - 79s 1ms/step - loss: 0.2630 - acc: 0.9195 - val_loss: 0.0574 - val_acc: 0.9825
#Epoch 2/12
#60000/60000 [==============================] - 77s 1ms/step - loss: 0.0900 - acc: 0.9730 - val_loss: 0.0437 - val_acc: 0.9855
#Epoch 3/12
#60000/60000 [==============================] - 78s 1ms/step - loss: 0.0663 - acc: 0.9810 - val_loss: 0.0387 - val_acc: 0.9874
#Epoch 4/12
#60000/60000 [==============================] - 76s 1ms/step - loss: 0.0555 - acc: 0.9836 - val_loss: 0.0321 - val_acc: 0.9881
#Epoch 5/12
#60000/60000 [==============================] - 76s 1ms/step - loss: 0.0462 - acc: 0.9862 - val_loss: 0.0287 - val_acc: 0.9907
#Epoch 6/12
#60000/60000 [==============================] - 81s 1ms/step - loss: 0.0418 - acc: 0.9873 - val_loss: 0.0318 - val_acc: 0.9893
#Epoch 7/12
#60000/60000 [==============================] - 81s 1ms/step - loss: 0.0364 - acc: 0.9885 - val_loss: 0.0291 - val_acc: 0.9907
#Epoch 8/12
#60000/60000 [==============================] - 80s 1ms/step - loss: 0.0338 - acc: 0.9898 - val_loss: 0.0260 - val_acc: 0.9922
#Epoch 9/12
#60000/60000 [==============================] - 80s 1ms/step - loss: 0.0319 - acc: 0.9903 - val_loss: 0.0266 - val_acc: 0.9918
#Epoch 10/12
#60000/60000 [==============================] - 79s 1ms/step - loss: 0.0290 - acc: 0.9908 - val_loss: 0.0271 - val_acc: 0.9919
#Epoch 11/12
#60000/60000 [==============================] - 79s 1ms/step - loss: 0.0281 - acc: 0.9911 - val_loss: 0.0247 - val_acc: 0.9928
#Epoch 12/12
#60000/60000 [==============================] - 82s 1ms/step - loss: 0.0256 - acc: 0.9920 - val_loss: 0.0251 - val_acc: 0.9926
#<keras.callbacks.History at 0x182f48b128>


# In[9]:


# 5. 预测
score = model.evaluate(x_test, y_test, verbose=0) # 在测试集上测试

#Test loss:  0.025120523367086936
#Test accuracy:  0.9926
print('Test loss: ', score[0])
print('Test accuracy: ', score[1])


# In[10]:


model.save('.\model\HandwritingRecUsingCNN.model') # 保存模型

