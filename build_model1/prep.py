caller_method = open('test_call_methods.txt','r').readlines()
name_method = open('test_method_name.txt','r').readlines()

output_file = open('data01.csv','w')
output_file.write('caller_method,name_method\n')
name_method_result = []
for i in range(len(name_method)):
    if ',' in name_method[i]:
        res = name_method[i].replace('[','').replace(']','').replace('\', \'','')[1:-2]
    else:
        res = name_method[i][:-1]
    caller_method_split = caller_method[i].split(', ')
    for j in range(len(caller_method_split)):
        rex = None
        if 'None' in caller_method_split[j]:
            rex = 'None'
        elif j==0 and len(caller_method_split)!=1: 
            rex = caller_method_split[j][2:-1]
        elif j==0 and len(caller_method_split)==1: 
            rex = caller_method_split[j][2:-3]
        elif j==len(caller_method_split)-1:
            rex = caller_method_split[j][1:-3]
        else:
            rex = caller_method_split[j][1:-1]
        print(rex,res)
        output_file.write(rex+','+res+'\n')