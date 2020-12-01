path = 'AbstractAllocator.java'



#MethodInvocation

#MethodDeclaration

# def checkMethodDeclaration(content,l_block,r_block,str_x):
#     prev_block = l_block
#     if '{' in str_x:
#         l_block = l_block + 1
#     if '}' in str_x:
#         r_block = r_block + 1
#     if l_block != r_block:
#         if l_block == 1 and r_block == 0 and prev_block == 0:
#             content = content
#         else:
#             content = content + str_x
#     if l_block == r_block and l_block != 0:
#         return True, content, l_block, r_block
#     else:
#         return False, content, l_block, r_block

content = ''
l_block = 0
r_block = 0


# for i in range(len(f)):
#     if ';' in f[i]:
#         if 'package' in f[i]:
#             print(i+1,i+1,'package')
#         if 'import' in f[i]:
#             print(i+1,i+1,'import')
#     elif ' class ' in f[i]:
#         print(i+1,i+1,'class')
    # c_declaration, content, l_block, r_block = checkMethodDeclaration(content, l_block, r_block, f[i])
    
def checkParenthesis(str_x):
    res = 0
    l_block = 0
    r_block = 0
    for i in str_x:
        if '{' in i:
            l_block = l_block + 1
        if '}' in i:
            r_block = r_block + 1
        if l_block == r_block and l_block != 0:
            return res
        res = res + 1
    return None

def checkMethodByLine(f,line):
    if line == None:
        return len(f)
    elif '@Override' in f[line]:
        print(line+1,line+1,'@Override')
        return line+1
    elif len(f[line].strip()) == 0:
        print(line+1,line+1,'empty')
        return line+1
    elif '*' in f[line]:
        num_comments = 0
        for i in f[line:]:
            if '*' in i:
                num_comments = num_comments + 1
            else:
                break
        print(line+1,line+num_comments,'comment')
        return line+num_comments
    elif '//' in f[line]:
        num_comments = 0
        for i in f[line:]:
            if '//' in i:
                num_comments = num_comments + 1
            else:
                break
        print(line+1,line+num_comments,'comment')
        return line+num_comments
    elif ';' in f[line]:
        if 'package' in f[line]:
            print(line+1,line+1,'package')
        elif 'import' in f[line]:
            print(line+1,line+1,'import')
        else:
            print(line+1,line+1,'MethodInvocation')
        return line+1
    elif 'public ' in f[line]:
        if ' class ' in f[line]:
            num_line = checkParenthesis(f[line:])
            print(line+1,line+1+num_line,'public class')
            return line+1+1
        else:
            num_line = checkParenthesis(f[line:])
            print(line+1,line+1+num_line,'MethodDeclaration')
            return line+1+num_line
    elif 'private ' in f[line]:
        if ' class ' in f[line]:
            num_line = checkParenthesis(f[line:])
            print(line+1,line+1+num_line,'private class')
            return line+1+1
        else:
            num_line = checkParenthesis(f[line:])
            print(line+1,line+1+num_line,'MethodDeclaration')
            return line+1+num_line

f = open(path).readlines()
print('start_line','end_line','method')
counter = 0
for i in range(len(f)):
    if counter == len(f):
        break
    # print(counter)
    next_cursor = checkMethodByLine(f,counter)
    counter = next_cursor
    

