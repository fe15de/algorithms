from collections import deque

class Node:
    data = None
    left = None
    right = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class BinaryTree:
    
    def __init__(self,root):
        self.root = root


'''
        TODO 
Implement a method to add nodes to the tree 
'''

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
    
    def breath_search(self):
    # It's like a search in levels 
    # it finishes searching a level of the tree before going down more  
        if self.root == None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            
            if current.left != None: 
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
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

tree = BinaryTree(a)
tree.depth_search()
print('----------------------')
tree.breath_search()

