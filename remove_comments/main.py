file_input = open('result.txt','r').readlines()

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

def removeComments(strx):
    strx = strx.split()
    counter = 0
    f = False
    while counter < len(strx)-1:
        # print(strx[counter],counter,f)
        if strx[counter][:2]  == '/*':
            f = True
            strx[counter] = ''
        if strx[counter][:2] == '*/':
            f = False
            strx[counter] = strx[counter].replace('*/','')
        if f:
            strx[counter] = ''
        counter = counter + 1
    strx = ' '.join([str(elem) for elem in strx])
    return strx

counter = 0
for i in file_input:
    if counter == 198:
        print(i)
        j = removeComments(i)
        print(j)
    counter = counter + 1
