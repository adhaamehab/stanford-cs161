import numpy as np
# Implementation of unweighted undirected graphs with edges that point to a "superEdge"

class CS161Vertex:
    def __init__(self, v):
        self.neighbors = [] # list CS161Edges incident on this vertex
        self.value = v
        self.superNode = None
        self.visited = False
    
    def getEdge(self,v):
        for E in self.neighbors:
            x,y = E.endpts
            if x == v or y == v:
                return E
        return None
    
    def getNeighbors(self):
        ret = []
        for E in self.neighbors:
            u,v = E.endpts
            if u != self:
                ret.append(u)
            if v != self:
                ret.append(v)
        return ret
    
    def addNeighbor(self,v,val=None):
        E = CS161Edge(u,v,val=val)
        self.addEdge(E)
        return E
    
    def addEdge(self,E):
        self.neighbors.append(E)
    
    def __str__(self):
        if hasattr(self.value, '__iter__'):
            return str([ str(x) for x in self.value ])
        return str(self.value) 
        
class CS161Edge:
    def __init__(self,u,v,val=None):
        self.endpts = (u,v)
        self.value = val
        
    def __str__(self):
        u,v = self.endpts
        if hasattr(self.value, '__iter__'):
            valStr = str([ str(x) for x in self.value ])
        else:
            valStr = str(self.value) 
        return str(u) + "," + str(v) + ":" + valStr
        
# This is an undirected graph class for use in CS161.
class CS161Graph:
    def __init__(self):
        self.vertices = []
        
    def addVertex(self,n):
        self.vertices.append(n)
        
    def removeVertex(self,n):
        self.vertices.remove(n)
        for E in n.neighbors:
            u,v = E.endpts
            u.neighbors.remove(E)
            v.neighbors.remove(E)
                
        
    # add an undirected edge from CS161Node u to CS161Node v
    def addEdge(self,u,v,val=None):
        E = CS161Edge(u,v,val=val)
        u.addEdge(E)
        v.addEdge(E)
 
    # get a list of all the edges
    # edges are a list of two vertices and a pointer to the superEdge it belongs to
    def getEdges(self):
        ret = []
        for v in self.vertices:
            v.visited = False
        for v in self.vertices:
            v.visited = True
            for E in v.neighbors:
                x,y = E.endpts
                if x.visited == False or y.visited == False:
                    ret.append( E )
        return ret
    
    def __str__(self):
        ret = "CS161Graph with:\n"
        ret += "\t Vertices:\n\t"
        for v in self.vertices:
            ret += str(v) + ","
        ret += "\n"
        ret += "\t Edges:\n\t"
        for E in self.getEdges():
            ret += "(" + str(E) + ") "
        ret += "\n"
        return ret
    

