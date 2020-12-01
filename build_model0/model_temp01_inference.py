from tensorflow.keras.models import load_model 
import pandas as pd 

model = load_model('model_temp01.h5')

print(model.summary())

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
predictions = model.predict(X)
index = 0
index_arr = []

actual = [] 
for i in open('data/method_name.txt','r').readlines():
    i = i.replace('\',\'','')[:-1].replace(']','').replace('\'','').replace('[','').replace(', ','')
    actual.append(i)
print(actual,len(actual))
# c = 0
for i in range(len(actual)):
    x = np.argmax(predictions[i])
    r = name_class_arr[x]
    print('Expected: ',actual[i],' | Predicted: ',r)
print(predictions.shape)