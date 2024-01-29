import random
from tree import BinarySearchTree

random.seed(20)

values = random.sample(range(1, 1000), 50)

bst = BinarySearchTree()
for v in values:
  bst.insert(v) 
  
bst.inorder_traversal()

items = [1, 28, 104, 928, 325]
for item in items:
  r = bst.search(item)
  if r is None:
    print(item, 'not found')
  else:
    print(r.root.data, 'found')
