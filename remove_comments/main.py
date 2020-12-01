file_input = open('result.txt','r').readlines()

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

def removeComments(strx):
    f = False
    res = ''
    for i in range(len(strx)-1):
        if strx[i:i+2] == '/*':
            f = True
        if strx[i:i+2] == '*/':
            f = False
        if not f:
            res = res + strx[i]
    res = res.replace('*/','')
    return res

counter = 0
for i in file_input:
    if counter == 198:
        print(i)
        j = removeComments(i)
        print(j)
    counter = counter + 1
