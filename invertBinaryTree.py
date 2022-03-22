#iterative --approach


def invertBinaryTree(tree):
    queue=[tree]
	while len(queue) >0:
		current=queue.pop(0)
		
		if current is None:
			continue
		swapFunction(current)
		queue.append(current.left)
		queue.append(current.right)
		
def swapFunction(tree):
	tree.left, tree.right=tree.right, tree.left
  
  #recursive approach
  
  def invertBinaryTree(tree):
	if tree is None:
		return
	swapFunction(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
    
	
def swapFunction(tree):
	tree.left, tree.right=tree.right, tree.left
