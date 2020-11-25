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

print('XXXX')
i = 0 
for path, node in tree:
    if i!=0:
        if isinstance(node,MethodDeclaration):
            print('---')
            print(node)
            print('---')
            print(node.type_parameters)
            print('---')
            print(node.return_type)
            print('---')
            print(node.name)
            print('---')
            print(node.parameters)
            print('---')
            print(node.throws)
            print('---')
            print(node.body)
            print('---')
            print(node.children)
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
