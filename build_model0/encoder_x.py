# sbt = open('data/sbt.txt','r').readlines()
# print('Input 01: ',sbt[0])

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
output_str = []
import numpy as np

import string
vocab = sorted(set(string.printable))
char2idx = {u:j for j, u in enumerate(vocab)}
idx2char = np.array(vocab)


for i in output_list:
    t = ''.join([str(elem) for elem in i]) 
    output_str.append(t)
    
    tt = np.array([char2idx[c] for c in t])
    ttt = np.array([idx2char[c] for c in tt])
    ttt = ''.join([str(elem) for elem in ttt]) 
    print('{} ---- characters mapped to int ---- > {}'.format(t, tt))
    print('{} ---- characters mapped to string ---- > {}'.format(tt, ttt))
    # print(i,t)