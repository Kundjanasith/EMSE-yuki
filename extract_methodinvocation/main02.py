import json 

input_file = open('cassandla.ast.json','r').readlines()
output_file = open('output1.txt','w')

for i in range(len(input_file)):
    print(input_file[i][1:-2])
    temp_txt = input_file[i][1:-2]
    t = temp_txt.split('}, {')
    res_str = []
    for j in range(len(t)):
        if j == 0 and len(t) != 1:
            res_str.append(t[j]+'}')
        elif j == 0 and len(t) == 1:
            res_str.append(t[j])
        elif j == len(t)-1:
            res_str.append('{'+t[j])
        else:
            res_str.append('{'+t[j]+'}')
    results = []
    for r in res_str:
        print('--',r)
        jx = json.loads(r)
        if jx['type'] == 'MethodInvocation':
            results.append(jx['value'])
    if len(results) == 0:
        output_file.write(str([None])+'\n')
    else:
        output_file.write(str(results)+'\n')
    # break
