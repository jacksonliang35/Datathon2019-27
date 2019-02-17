
# coding: utf-8

# In[108]:

import tensorflow as tf
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import Sequential
from keras.layers import LSTM,Dense
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dropout
#import matplotlib.pyplot as plt




data = pd.read_csv("C:\\Users\\15121\\Desktop\\Datathon2019-27-master\\Data Given\\SYF.csv")
#test=pd.read_csv("C:\\Users\\15121\\Desktop\\Datathon2019-27-master\\Data Given\\test2019.csv",sep=",")
# cl = data.Close
cl = data.drop("Date", axis=1).dropna()


# In[109]:

scl = MinMaxScaler()
#Scale the data
cl = cl.values.reshape(cl.shape[0], cl.shape[1])
cl = scl.fit_transform(cl)
DIM = 6
PREV = 30
def processData(data,lb):
    X,Y = [], []
    for i in range(len(data)-lb-1):
        xtemp, ytemp = [], []
        #for j in range(DIM):
        xtemp.extend(data[i:(i+lb),[0,1,2,4,5]])
        ytemp.append(data[(i+lb),3])
        X.append(xtemp)
        Y.append(ytemp)
    return np.array(X),np.array(Y)
X,y = processData(cl,PREV)
X_train,X_test = X[:int(X.shape[0]*0.80)],X[int(X.shape[0]*0.80):]
y_train,y_test = y[:int(y.shape[0]*0.80)],y[int(y.shape[0]*0.80):]
print(X_train.shape[0])
print(X_test.shape[0])
print(y_train.shape[0])
print(y_test.shape[0])


# In[110]:

dim=X.shape


# In[111]:

model = Sequential()
model.add(LSTM(256,input_shape=(PREV,5)))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')
#Reshape data for (Sample,Timestep,Features)
X_train = X_train.reshape((X_train.shape[0],X_train.shape[1],5))
X_test = X_test.reshape((X_test.shape[0],X_test.shape[1],5))
#Fit model with history to check for overfitting
history = model.fit(X_train,y_train,epochs=10,validation_data=(X_test,y_test),shuffle=False)


# In[112]:

x=X[dim-23:]
x = x.reshape((23,30,5))
Xt=model.predict(x)
z = np.zeros((23,2))
Xt=np.append(Xt,z, axis=1)
z=np.zeros((23,3))
Xt=np.append(z,Xt,axis=1)
w=scl.inverse_transform(Xt)
w[:,3]


# In[ ]:



