class InOneLine:

    # path = 'C:\\Users\\acmil\\Desktop\\Antlr\\Research\\dataset\\test\\cassandra\\AbstractAllocator.java'
    # path = 'C:/Users/yuki-fu/Desktop/dataset/test/cassandra/AbstractAllocator.java'
    # path = 'C:/Users/yuki-fu/Desktop/dataset/test/cassandra/AbstractBTreePartition.java'
    # def getPath(path):
    #     print('------------------')
    #     print(path)
    #     print('------------------')
    #     return path
    
    # @classmethod
    # def extractMethod(line, path):
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
                # if f[line][*] or f[line].startwith('/*') or f[line].startwith('*/'):
                if '*' in f[line]:
                    num_comments = 0
                    for i in f[line:]:
                        if '*' in i:
                            num_comments = num_comments + 1
                        else:
                            break
                    # print(line+1,line+num_comments,'comment')
                    # print('comment')
                if '//' in f[line]:
                    num_comments = 0
                    for i in f[line:]:
                        if '//' in i:
                            num_comments = num_comments + 1
                        else:
                            break
                    # print(line+1,line+num_comments,'comment')
                    # print('comment')
                # if '//' in f[line]:
                #     comment_position = f[line].find('//')
                #     print('comment_position:{}'.format(comment_position))
                #     context = context + f[i][:comment_position]
                content = content + f[i]
                # print(content)
                break
            # for MethodDeclaration
            else:
                # count l_clock
                m_block = l_block
                if '{' in f[i]:
                    # if '//' in f[line]:
                    #     comment_position = f[line].find('//')
                    #     print('comment_position:{}'.format(comment_position))
                    #     context = context + f[i][:comment_position]
                    l_block = l_block + 1
                    #  count r_block
                if '}' in f[i]:
                    # if '//' in f[line]:
                    #     comment_position = f[line].find('//')
                    #     print('comment_position:{}'.format(comment_position))
                    #     context = context + f[i][:comment_position]
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
                    # if '//' in f[line]:
                    #     comment_position = f[line].find('//')
                    #     print('comment_position:{}'.format(comment_position))
                    #     context = context + f[i][:comment_position]
                    content = content + f[i]
                # print(i,l_block,r_block,f[i][:-1])
                # print(f[i][:-1])
                if l_block == r_block and l_block != 0:
                    # if '//' in f[line]:
                    #     comment_position = f[line].find('//')
                    #     print('comment_position:{}'.format(comment_position))
                    #     context = context + f[i][:comment_position]
                    content = content + f[i]
                    # print(content)
                    break
        # print(content)
        method_list = content.split()
        # print(method_list)
        for i in method_list:
            # print(i)
            oneLine = oneLine + i + ' '
        # print(oneLine)
        
        return oneLine

    # print(extractMethod(48, path))
    
    


# ###############################
# content = ''
# l_block = 0
# r_block = 0
# f = open(path).readlines()

# for i in range(33,len(f)):
#     if ';' in f[33]:
#         content = content + f[i]
#         print(content)
#         break

#     else:
#         if '{' in f[i]:
#             l_block = l_block + 1
#         if '}' in f[i]:
#             r_block = r_block + 1
#         if l_block != r_block:
#             content = content + f[i]
#         # print(i,l_block,r_block,f[i][:-1])
#         print(f[i][:-1])
#         if l_block == r_block and l_block != 0:
#             # print(content)
#             break
# #############################





# l_brock_num = 0
# r_brock_num = 0

# # start_line = 0
# start_line = 33

# methodbody = ''

# with open(path) as f:
#     l = f.readlines()

#     for i in range(100):
#         # print(l[i])
#         print(i)
#         if i == start_line:
#             if ';' in l[i]:
#                 print('MethodInvocation')
#                 print(l[i])
#                 print('i = {}'.format(i))
#                 # i+=1
#             else:
#                 print('MethodDeclaration')
#                 if '{' in l[i]:
#                     l_brock_num += 1
#                     print(l[i])
#                     print('a')
#                     i+=1
#                     print('i = {}'.format(i))
#                     # start_line+=1
#                 elif '}' in l[i]:
#                     r_brock_num += 1
#                     print(l[i])
#                     print('b')
#                     i+=1
#                     print('i = {}'.format(i))
#                     # start_line+=1
#                     if l_brock_num == r_brock_num:
#                         print('修了')
#                 else:
#                     print(l[i])
#                     print('c')
#                     i+=1
#                     print('i = {}'.format(i))
#                     # start_line+=1

#     print(l[start_line])



    # if ';' in l[start_line]:
    #     print('MethodInvocation')
    #     print(l[start_line])
    #     start_line+=1
    #     # methodbody = methodbody + l[start_line] + ' '
    #     # print(methodbody)
    # else:
    #     print('MethodDeclaration')
    #     # methodbody = methodbody + l[start_line] + ' '
    #     # print(methodbody)
    #     if '{' in l[start_line]:
    #         l_brock_num += 1
    #         print(l[start_line])
    #         print('a')
    #         start_line+=1
    #         # start_line += 1
    #         # methodbody = methodbody + l[start_line] + ' '
    #     elif '}' in l[start_line]:
    #         r_brock_num += 1
    #         print(l[start_line])
    #         # methodbody = methodbody + l[start_line] + ' '
    #         print('b')
    #         start_line+=1
    #         if l_brock_num == r_brock_num:
    #             print('修了')
    #     else:
    #         print(l[start_line])
    #         print('c')
    #         start_line+=1
            # methodbody = methodbody + l[start_line] + ' '
            # print(methodbody)
            