path = 'AbstractBTreePartition.java'
f = open(path).readlines()
import sys


l_block = 0
r_block = 0

file_out = open('Post_AbstractBTreePartition.java','w')
counter = 0
for i in range(len(f)):
    if counter == len(f):
        break
    l_c = f[counter].count('(')
    r_c = f[counter].count(')')
    if '*' not in f[i]:
        if l_c != r_c:
            str_x = f[i]
            for j in range(counter+1,len(f)):
                l_c = l_c + f[j].count('(')
                r_c = r_c + f[j].count(')')
                str_x = str_x[:-1] + f[j][:-1]
                if l_c == r_c:
                    # print(str_x+'\n')
                    # print('----')
                    counter = j
                    break
                    
            file_out.write(str_x)
        else:
            file_out.write(f[i])
    else:
        file_out.write(f[i])
    counter = counter + 1

            
    