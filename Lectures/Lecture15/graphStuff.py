import numpy as np
# Implementation of directed graphs with weighted edges

class CS161Vertex:
    def __init__(self, v):
        self.inNeighbors = [] # list of pairs (nbr, wt), where nbr is a CS161Vertex and wt is a weight
        self.outNeighbors = [] # same as above
        self.value = v
        # useful things for Prim's algorithm
        self.estD = np.inf
        self.parent = None
        
    def hasOutNeighbor(self,v):
        if v in self.getOutNeighbors():
            return True
        return False
        
    def hasInNeighbor(self,v):
        if v in self.getInNeighbors():
            return True
        return False
    
    def hasNeighbor(self,v):
        if v in self.getInNeighbors() or v in self.getOutNeighbors():
            return True
        return False
    
    def getOutNeighbors(self):
        return [ v[0] for v in self.outNeighbors ]
    
    def getInNeighbors(self):
        return [ v[0] for v in self.inNeighbors ]
        
    def getOutNeighborsWithWeights(self):
        return self.outNeighbors
    
    def getInNeighborsWithWeights(self):
        return self.inNeighbors
        
    def addOutNeighbor(self,v,wt):
        self.outNeighbors.append((v,wt))
    
    def addInNeighbor(self,v,wt):
        self.inNeighbors.append((v,wt))
    
    def __str__(self):
        return str(self.value) 
        
# This is a directed graph class for use in CS161.
# It can also be used as an undirected graph by adding edges in both directions.
class CS161Graph:
    def __init__(self):
        self.vertices = []
        
    def addVertex(self,n):
        self.vertices.append(n)
        
    # add a directed edge from CS161Node u to CS161Node v
    def addDiEdge(self,u,v,wt=1):
        u.addOutNeighbor(v,wt=wt)
        v.addInNeighbor(u,wt=wt)
    
    # add edges in both directions between u and v
    def addBiEdge(self,u,v,wt=1):
        self.addDiEdge(u,v,wt=wt)
        self.addDiEdge(v,u,wt=wt)

    # get a list of all the directed edges
    # directed edges are a list of two vertices and a weight
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            for u, wt in v.getOutNeighborsWithWeights():
                ret.append( [v,u,wt] )
        return ret
    
    def __str__(self):
        ret = "CS161Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b,wt in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + "; wt:" + str(wt) + ") "
        ret += "\n"
        return ret
    
class CS161Graph:
    def __init__(self):
        self.vertices = []
        
    def addVertex(self,n):
        self.vertices.append(n)
        
    # add a directed edge from CS161Node u to CS161Node v
    def addDiEdge(self,u,v,wt=1):
        u.addOutNeighbor(v,wt=wt)
        v.addInNeighbor(u,wt=wt)
    
    # add edges in both directions between u and v
    def addBiEdge(self,u,v,wt=1):
        self.addDiEdge(u,v,wt=wt)
        self.addDiEdge(v,u,wt=wt)

    # get a list of all the directed edges
    # directed edges are a list of two vertices and a weight
    def getDirEdges(self):
        ret = []
        for v in self.vertices:
            for u, wt in v.getOutNeighborsWithWeights():
                ret.append( [v,u,wt] )
        return ret
    
    def __str__(self):
        ret = "CS161Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b,wt in self.getDirEdges():
            ret += "(" + str(a) + "," + str(b) + "; wt:" + str(wt) + ") "
        ret += "\n"
        return ret


        


