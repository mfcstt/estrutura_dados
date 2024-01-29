from tree import BinaryTree, Node

def pos_ordem_example_tree():
  tree = BinaryTree()
  n1 = Node(0)
  n2 = Node(1)
  n3 = Node(2)
  n4 = Node(3)
  n5 = Node(4)
  n6 = Node(5)
  
  n1.left = n2
  n1.right = n3
  n2.left = n4
  n2.right = n5
  n3.left = n6
    
  tree.root = n1
  return tree

if __name__ == "__main__":
  tree = pos_ordem_example_tree()
  print("Percurso em pós ordem")
  tree.pos_order_traversal()
  print("Altura da árvore: ", tree.height())