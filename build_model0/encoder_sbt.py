sbt = open('data/sbt.txt','r').readlines()

import string
import numpy as np
vocab = sorted(set(string.printable))
char2idx = {u:j for j, u in enumerate(vocab)}
idx2char = np.array(vocab)

output_file = open('encoder/sbt.txt','w')
res = []
for i in sbt:
    r = np.array([char2idx[c] for c in i])
    res.append(r)
    # res = ','.join([str(elem) for elem in r]) 
    # output_file.write('['+str(res)+']\n')
res = np.array(res)
np.savetxt('encoder/sbt.txt', res, delimiter=',') 