import string
import numpy as np
vocab = sorted(set(string.printable))
char2idx = {u:j for j, u in enumerate(vocab)}
idx2char = np.array(vocab)

sbt = open('data/sbt.txt','r').readlines()
sbt_res = []
for i in sbt:
    r = np.array([char2idx[c] for c in i])
    sbt_res.append(r)
sbt_res = np.array(sbt_res)
caller_method = open('data/caller_method.txt','r').readlines()
caller_res = []
for i in caller_method:
    r = np.array([char2idx[c] for c in i])
    caller_res.append(r)
caller_res = np.array(caller_res)
method_name = open('data/method_name.txt','r').readlines()
output_list = []
for m in method_name:
    if ',' not in m:
        output_list.append([m[:-1]])
    else:
        temp = []
        mm = m.split(',')
        for k in range(len(mm)):
            if k==0:
                temp.append(mm[k][2:-1])
            elif k==len(mm)-1:
                temp.append(mm[k][2:-3])
            else:
                temp.append(mm[k][2:-1])
        output_list.append(temp)
name_res = []
for i in output_list:
    t = ''.join([str(elem) for elem in i]) 
    tt = np.array([char2idx[c] for c in t])
    name_res.append(tt)
name_res = np.array(name_res)
print(sbt_res.shape)
print(caller_res.shape)
print(name_res.shape)

max_sbt_res = 0
for i in sbt_res:
    if max_sbt_res < i.shape[0]:
        max_sbt_res = i.shape[0]
print(max_sbt_res)

max_caller_res = 0
for i in caller_res:
    if max_caller_res < i.shape[0]:
        max_caller_res = i.shape[0]
print(max_caller_res)

max_name_res = 0
for i in name_res:
    if max_name_res < i.shape[0]:
        print(i)
        max_name_res = i.shape[0]
print(max_name_res)


print(np.max(name_res))