import sys   # system we use it to defind infinity +00
import heapq     # package of list
class edge:
    def __init__(self,weight,start,target):
        self.weight=weight
        self.start=start    #biginnig of the way
        self.target=target   #our target node
class nod:
    def __init__(self,data):
        self.data=data #data of the node
        self.visited=False  #the node is not visited yet
        self.predecessor=None #parent of the node
        self.mindistance=sys.maxsize #plus infini +00
        self.adjacencieslist=[]  #children of the node
    def __cmp__(self, othervertex):
        return self.cmp(self.mindistance,othervertex.mindistance)
    def __lt__(self, other):
        return self.mindistance<other.mindistance
class algorithm:
    def calcul_shortest_path(self,vertexlist,startvertext):
        q=[]
        startvertext.mindistance=0
        heapq.heappush(q,startvertext)#append
        while len(q)>0:
            actual_vertex=heapq.heappop(q)
            for edge in actual_vertex.adjacencieslist:
                u=edge.start
                v=edge.target
                new_distance=u.mindistance+edge.weight
                if new_distance<v.mindistance:
                    v.predecessor=u
                    v.mindistance=new_distance
                    heap.heappush(q,v)
    def get_shortest_path(self,target):
        node=target
        while node is not None:
            print(node.data)
            node=node.predecessor








