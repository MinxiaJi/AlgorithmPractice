# binary tree
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class bt(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def search(self,start,find_val):
        return self.search_helper(self.root,find_val)
    
    def search_helper(self,start,find_val):
        if start:
            if find_val == start.value:
                return True
            else:
                return self.search_helper(start.left,find_val) or self.search_helper(start.right,find_val)
        return False
    def print_path(self,start,traversal):
        return self.print_path_helper(self.root,'')[:-1]
    def print_path_helper(self,start,traversal):
        if start:
            traversal+= str(start.value)+'-'
            traversal = self.print_path_helper(start.left,traversal)
            traversal = self.print_path_helper(start.right,traversal)
        return traversal

tree = bt(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(tree.root,4))
# Should be False
print(tree.search(tree.root,6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_path(tree.root,''))
			

