class Node:
    data = None
    left = None
    right = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class binary_tree:
    
    def __init__(self,root):
        self.root = root

    def depth_search(self):
        
        if self.root == None:
            return
        
        stack = [self.root]
        while stack:
            current = stack.pop() 
            if current.right != None: 
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)
            print(current)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

tree = binary_tree(a)
tree.depth_search()

