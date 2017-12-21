# Implementation of directed, unweighted graphs for CS161

class CS161Vertex:
    def __init__(self, v):
        self.inNeighbors = []
        self.outNeighbors = []
        self.value = v
        # you can add attributes for vertices here!  For example:
        self.status = "unvisited" 
        self.color = None # may be useful...

    # below are a bunch of methods for interacting with CS161Vertices: 
    def hasOutNeighbor(self,v):
        if v in self.outNeighbors:
            return True
        return False
        
    def hasInNeighbor(self,v):
        if v in self.inNeighbors:
            return True
        return False
    
    def hasNeighbor(self,v):
        if v in self.inNeighbors or v in self.outNeighbors:
            return True
        return False
    
    def getOutNeighbors(self):
        return self.outNeighbors
    
    def getInNeighbors(self):
        return self.inNeighbors
        
    def addOutNeighbor(self,v):
        self.outNeighbors.append(v)
    
    def addInNeighbor(self,v):
        self.inNeighbors.append(v)
    
    def __str__(self):
        return str(self.value) 
        
# Directed, unweighted graph class for CS161. 
class CS161Graph:
    def __init__(self):
        # this is a list of CS161Vertices.  
        self.vertices = [] 
        # Each CS161Vertex knows who its neighbors are.

    # Add a vertex to the graph
    def addVertex(self,n):
        self.vertices.append(n)
        
    # add a directed edge from CS161Vertex u to CS161Vertex v
    def addDiEdge(self,u,v):
        u.addOutNeighbor(v)
        v.addInNeighbor(u)
    
    # add edges in both directions between u and v
    def addBiEdge(self,u,v):
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)
        
    # get a list of all the directed edges
    # directed edges are represented as a list of two vertices
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            ret += [ [v, u] for u in v.outNeighbors ]
        return ret
    
    # print out the vertices and edges in the graph
    def __str__(self):
        ret = "CS161Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + ") "
        ret += "\n"
        return ret
