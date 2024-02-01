import random
from tree import BinarySearchTree

random.seed(20)

def random_tree():
    values = random.sample(range(1, 1000), 50)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree
 
 #Percuso em nivel 
def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

bst = example_tree()
#bst.levelorder_traversal()

print("\n")
print("Max: ", bst.max())
print("Min: ", bst.min())


  

# Busca Binaria
#items = [1, 28, 104, 928, 325]
#for item in items:
#  r = bst.search(item)
# if r is None:
# print(item, 'not found')
# else:
# print(r.root.data, 'found')
