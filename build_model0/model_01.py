import string
import numpy as np
vocab = sorted(set(string.printable))
char2idx = {u:j for j, u in enumerate(vocab)}
idx2char = np.array(vocab)

sbt = open('data/sbt.txt','r').readlines()
sbt_res = []
for i in sbt:
    r = np.array([char2idx[c] for c in i])
    print(r.shape)
    sbt_res.append(r)
sbt_res = np.array(sbt_res)
print(sbt_res.shape)