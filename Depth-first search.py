class Node:
    def __init__(self,data):
        self.data=data
        self.adjacencyList=[]
        self.visited=False

class dep:
    def dfs(self,start_node):
        start_node.visited=True
        print(start_node.data)
        for n in start_node.adjacentlist:
            if not n.visited:
                self.dfs(n)
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

dfs = dep()
dfs.dfs(node1)
