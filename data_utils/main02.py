import javalang
import sys 
from javalang.tree import MethodDeclaration
from javalang.tree import ClassDeclaration
from javalang.tree import ConstructorDeclaration

input_path = sys.argv[1]
print('Input path: ', input_path)
file_data = open(input_path,'r').read()
print(len(file_data))

tree = javalang.parse.parse(file_data)

def astx(nodex):
    print('YEAH')
    print(node.name)
    print(node.name)

print('XXXX')
i = 0 
for path, node in tree:
    if i!=0:
        if isinstance(node,MethodDeclaration):
            print('---')
            print(node)
            print('---')
            astx(node)
            break
        if isinstance(node,ConstructorDeclaration):
            print('---')
            print(node)
            print('---')
            break
    i = i + 1
    # if i == 15:
    #     break
