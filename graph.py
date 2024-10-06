class Edge:
    previous = None
    next = None
    weight = None
    def __init__(self, previous, next, weight = 0):
        self.previous = previous
        self.next = next
        self.weight = weight

    def __repr__(self):
        return f'Node from: {self.previous}, Node to: {self.next}, Weight: {self.weight}'

class Vertex:
    index = None
    name = None
    
    def __init__(self,index,name):
        self.index = index
        self.name = name

    def __repr__(self):
        return f'index :{self.index}, name {self.name}'

class Graph:
    def __init__(self):    
        self.nodes = []
        self.edges = []
        self.current_index = 0

    def insert_edge(self,previous,next,weight=0):
        vertex_previous = None
        vertex_next = None

        for node in self.nodes:
            if node.name == previous:
                vertex_previous = node 
            if node.name == next:
                vertex_next = node
        

        if vertex_previous == None:
            vertex_previous = Vertex(self.current_index, previous)
            self.current_index += 1
            self.nodes.append(vertex_previous)
        
        if vertex_next == None:
            vertex_next = Vertex(self.current_index, next)
            self.current_index += 1
            self.nodes.append(vertex_next)
        

        self.edges.append(Edge(vertex_previous,vertex_next,weight)) 

    def DFS(self,):
      pass 

    def view(self):
        for edge in self.edges:
            print(edge)

g = Graph()
g.insert_edge("A", "B", 1.5)
g.insert_edge("A", "C", 1)
g.insert_edge("A", "D", 2.7)
g.insert_edge("C", "D", 3.5)
g.insert_edge("D", "E", 1.1)
g.insert_edge("D", "F", 1.5)
g.view()
