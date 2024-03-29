from queue import Queue

ROOT = "root"

class Node:
  
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def __str__(self):
		return str(self.data)
	
class BinaryTree:
	def __init__(self, data=None, node=None):
		if node:
			self.root = node
		elif data:
			node = Node(data)
			self.root = node
		else:
			self.root = None
   
	def inorder_traversal(self, node=None):
		if node is None:
			node = self.root
		if node.left:
			self.inorder_traversal(node.left)
		print(node, end=' ')
		if node.right:
			self.inorder_traversal(node.right)
		
   
	def pos_order_traversal(self, node=None):
			if node is None:
				node = self.root
			if node.left:
				self.pos_order_traversal(node.left)
			if node.right:
				self.pos_order_traversal(node.right)
			print(node)
 
	def height(self, node=None):
		if node is None:
			node = self.root
		hleft = 0
		hright = 0 
		if node.left:
			hleft = self.height(node.left)
		if node.right:
			hright = self.height(node.right)
		if hright > hleft:
			return hright + 1
		return hleft + 1

	def levelorder_traversal(self, node=ROOT):
		if node == ROOT:
			node = self.root

		queue = Queue()
		queue.push(node)
		while len(queue):
			node = queue.pop()
			if node.left:
				queue.push(node.left)
			if node.right:
				queue.push(node.right)
			print(node, end=" ")
   

   

class BinarySearchTree(BinaryTree):
  
	def insert(self, value):
		parent = None
		x = self.root
		while(x):
			parent = x
			if value < x.data:
				x = x.left
			else:
				x = x.right
		if parent is None:
			self.root = Node(value)
		elif value < parent.data:
			parent.left = Node(value)
		else:
			parent.right = Node(value)
   
	def search(self, value):
			return self._search(value, self.root)
			
	def _search(self, value, node):
			if node is None:
				return node
			if node.data == value:
				return BinarySearchTree(node)
			if value < node.data:
				return self._search(value, node.left)
			return self._search(value, node.right)
 
	def min(self, node=ROOT):
		if node == ROOT:
			node = self.root
		while node.left:
			node = node.left
		return node.data

	def max(self, node=ROOT):
		if node == ROOT:
			node = self.root
		while node.right:
			node = node.right
		return node.data
  

     