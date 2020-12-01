def extractMethod(line, path):
    content = ''
    oneLine = ''
    l_block = 0
    r_block = 0
    f = open(path).readlines()
    # preprocess to delite commentout sentences
    for i in range(len(f)):
        if '//' in f[i]:
            f[i] = ''
    for i in range(line,len(f)):
        # for MethodInvocation
        if ';' in f[line]:
            if '*' in f[line]:
                num_comments = 0
                for i in f[line:]:
                    if '*' in i:
                        num_comments = num_comments + 1
                    else:
                        break
            if '//' in f[line]:
                num_comments = 0
                for i in f[line:]:
                    if '//' in i:
                        num_comments = num_comments + 1
                    else:
                        break
            content = content + f[i]
            break
        # for MethodDeclaration
        else:
            # count l_clock
            m_block = l_block
            if '{' in f[i]:
                l_block = l_block + 1
            if '}' in f[i]:
                r_block = r_block + 1
            if l_block == 1 and r_block == 0 and m_block == 0:
                ll_b = 0
                rr_b = 0
                xx_b = None
                for k in range(i-1,0,-1):
                    ll_b = ll_b + f[k].count('(')
                    rr_b = rr_b + f[k].count(')')
                    if ll_b == rr_b:
                        xx_b = k
                        break
                res_k = ''
                for k in f[xx_b:i]:
                    res_k = res_k + k[:-1]
                content = content + res_k
            if l_block != r_block:
                content = content + f[i]
            if l_block == r_block and l_block != 0:
                content = content + f[i]
                break
    method_list = content.split()
    for i in method_list:
        oneLine = oneLine + i + ' '
    return oneLine

print(extractMethod(0,'Annotations.java'))
            