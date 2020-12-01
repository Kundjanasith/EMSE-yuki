import pandas as pd 
from keras.utils import to_categorical

df = pd.read_csv('data_QA/data01.csv')
print(len(df))
df.dropna(inplace=True)
print(len(df))

caller_class = open('data_QA/caller_class.csv','w')
for i in df['caller_method'].value_counts().index.tolist():
    caller_class.write(i+'\n')
name_class = open('data_QA/name_class.csv','w')
for i in df['name_method'].value_counts().index.tolist():
    name_class.write(i+'\n')
caller_class_arr = df['caller_method'].value_counts().index.tolist()
name_class_arr = df['name_method'].value_counts().index.tolist()


caller_method = open('data/caller_method.txt','r').readlines()
print(len(caller_method))

name_method = open('data/method_name.txt','r').readlines()
print(len(name_method))

import numpy as np
X = []
for i in caller_method:
    # print(i)
    temp = np.zeros(len(caller_class_arr))
    for j in range(len(caller_class_arr)):
        if caller_class_arr[j] in i:
            temp[j] = 1
    X.append(temp)
y = []
for i in name_method:
    # print(i)
    temp = np.zeros(len(name_class_arr))
    for j in range(len(name_class_arr)):
        if name_class_arr[j] in i:
            temp[j] = 1   
    y.append(temp)  
X = np.array(X)
y = np.array(y)
print(X.shape,y.shape)    

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

from keras.callbacks import History 
history = History()

model = Sequential()
model.add(Dense(12, input_dim=X.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(y.shape[1], activation='sigmoid'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X,y,epochs=100,callbacks=[history])
model.save('model_temp01.h5')
print(len(history.history['loss']))

import matplotlib.pyplot as plt 
plt.plot(history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.savefig('loss_model_temp01.png',bbox_inches='tight')


