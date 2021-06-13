import sys
class node:
    def __init__(self,data):
        self.data=data
        self.arret=arret
        self.pradatacor=None
        self.landa=sys.maxsize
        self.arcs=[]
class arret:
    def __init__(self,wight,node_end):
        self.wight=wight
        self.end_node=node_end


class djikstra:
    def class_node(self,LIST):
        LIST[0].landa=0
        for i in LIST:
            for j in i.arcs:
                if j.end_node.landa>i.landa+j.wight:
                    j.end_node.landa =i.landa+j.wight
                    j.end_node.pradatacor=i

    def shortes_path(self,end_node,start_node):
        actual_pradatacor=end_node
        while actual_pradatacor!=start_node:
            print(actual_pradatacor.data)
            actual_pradatacor=actual_pradatacor.pradatacor
        print(start_node.data)





node1 = node("x1")

node2 = node("x2")
node3 = node("x3")
node4 = node("x4")
node5 = node("x5")

wight1=arret(3,node2)
wight2=arret(2,node3)
wight3=arret(5,node3)
wight4=arret(2,node4)
wight5=arret(3,node4)
wight6=arret(5,node5)
wight7=arret(7,node5)

node1.arcs.append(wight1)
node1.arcs.append(wight2)
node2.arcs.append(wight4)
node2.arcs.append(wight3)
node3.arcs.append(wight5)
node3.arcs.append(wight7)
node4.arcs.append(wight6)

djikstra1=djikstra()
djikstra1.class_node([node1,node2,node3,node4,node5])
djikstra1.shortes_path(node5,node1)
