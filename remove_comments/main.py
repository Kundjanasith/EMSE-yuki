file_input = open('result.txt','r').readlines()

def removeComments(strx):
    while '/*' in strx and '*/' in strx:
        l_inx = strx.index('/*')
        r_inx = strx.index('*/')
        strx = strx[:l_inx] + strx[r_inx+2:]
    return strx
    

counter = 0
for i in file_input:
    if counter == 198:
        print(i)
        j = removeComments(i)
        print(j)
    counter = counter + 1
