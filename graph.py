from collections import deque

#implementation with dictionary
class Graph:
   
    def __init__(self):
        self.graph = {}

    def add(self, key, value, weight):
        
        arguments = (value,weight)
        if key in self.graph:
            values = self.graph[key]
            values.append(arguments)
        else:
            self.graph[key] = [arguments]
    
    def dfs(self):
        if self.graph == {}:
            return
            
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.dfs_helper(node, visited)

    def dfs_helper(self,node,visited):

        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                if current in self.graph:
                    connections = self.graph[current]
                    for i in reversed(connections):
                        if i[0] not in visited:
                            stack.append(i[0])

    def bfs(self):

        if self.graph == {}:
            return

        visited = set()
        for node in self.graph:
            if node not in visited:
                self.bfs_helper(node, visited)
    
    def bfs_helper(self,node,visited):

        queue = deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            if current not in visited:
                print(current)
                visited.add(current)
                if current in self.graph:
                    connections = self.graph[current]
                    for i in connections:
                        if  i[0] not in visited:
                            queue.append(i[0])

    def __repr__(self):
        elements = ""
        for element in self.graph:
            elements += f'{element} -> {self.graph[element]}\n'
        return elements

g = Graph()
g.add("A", "B", 1.5)
g.add("A", "C", 1)
g.add("A", "D", 2.7)
g.add("C", "D", 3.5)
g.add("D", "E", 1.1)
g.add("D", "F", 1.5)
g.add("G", "F", 1.5)
# g.add("C", "G", 1.5)
print(g)
#TODO -> Add a better way to see bfs and dfs 
g.dfs()
print('----------------------------')
g.bfs()
# implementation with classes 
# class Edge:
#     previous = None
#     next = None
#     weight = None
#     def __init__(self, previous, next, weight = 0):
#         self.previous = previous
#         self.next = next
#         self.weight = weight
#
#     def __repr__(self):
#         return f'Node from: {self.previous}, Node to: {self.next}, Weight: {self.weight}'
#
# class Vertex:
#     index = None
#     name = None
#
#     def __init__(self,index,name):
#         self.index = index
#         self.name = name
#
#     def __repr__(self):
#         return f'index :{self.index}, name {self.name}'
#
# class Graph:
#     def __init__(self):    
#         self.nodes = []
#         self.edges = []
#         self.current_index = 0
#
#     def insert_edge(self,previous,next,weight=0):
#         vertex_previous = None
#         vertex_next = None
#
#         for node in self.nodes:
#             if node.name == previous:
#                 vertex_previous = node 
#             if node.name == next:
#                 vertex_next = node
#
#
#         if vertex_previous == None:
#             vertex_previous = Vertex(self.current_index, previous)
#             self.current_index += 1
#             self.nodes.append(vertex_previous)
#
#         if vertex_next == None:
#             vertex_next = Vertex(self.current_index, next)
#             self.current_index += 1
#             self.nodes.append(vertex_next)
#
#
#         self.edges.append(Edge(vertex_previous,vertex_next,weight)) 
#
#     def view(self):
#         for edge in self.edges:
#             print(edge)
#
# g = Graph()
# g.insert_edge("A", "B", 1.5)
# g.insert_edge("A", "C", 1)
# g.insert_edge("A", "D", 2.7)
# g.insert_edge("C", "D", 3.5)
# g.insert_edge("D", "E", 1.1)
# g.insert_edge("D", "F", 1.5)
# g.view()
