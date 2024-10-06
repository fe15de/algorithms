from collections import deque
import random

class Node:
    data = None
    left = None
    right = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f"Node data: {self.data}"

class BinaryTree:
    
    def __init__(self):
        self.root = None 

    def add(self,data):
        # Uses BFS
        new_node = Node(data)
    
        if self.root is None:
            self.root = new_node
            return
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def depth_first_search(self):
    #DFS
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
    
    def breath_first_search(self):
    #BFS
    # It's like a search in levels 
    # it finishes searching a level of the tree before going below 
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

    def search(self,key):
    # Aka tree includes 
    # search for a value with BFS
    # It can also be done with DFS 
        if self.root == None:
            return
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            if current.data == key:
                return 'Value found'

            if current.left != None: 
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            
        return 'Value not found'
    
    def search_recursive(self,root,key):
        if root == None:
            return False 
        if root.data == key:
            return True
    
        return self.search_recursive(root.left, key) or self.search_recursive(root.right, key) 

    def max_path_sum(self,root):
        
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return root.data
        
        max_value = max(self.max_path_sum(root.left) , self.max_path_sum(root.right))

        return root.data + max_value

    def min_value(self):
        
        if self.root == None:
            return

        lowest = self.root.data
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current.data < lowest:
                lowest = current.data

            if current.right != None: 
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)

        return lowest

    def tree_sum(self):
        total = 0

        if self.root == None:
            return
        
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            total += current.data
            if current.left != None: 
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

        return total

def main():
    tree = BinaryTree()

    for i in range(0,15):
        tree.add(random.randint(0,40))
    tree.depth_first_search()
    print('----------------------')
    tree.breath_first_search()
    print(f'search :{tree.search(3)}')
    print(f'recursive search : {tree.search_recursive(tree.root,3)}')
    print(f'max path sum :{tree.max_path_sum(tree.root)}')
    print(f'min value : {tree.min_value()}')
    print(f'tree sum : {tree.tree_sum()}')

main()
