path = 'AbstractAllocator.java'
f = open(path).readlines()


for i in range(len(f)):
    print('before',f[i])
    if '//' in f[i]:
        print('p')
        f[i] = ''
    print('after',f[i]) 