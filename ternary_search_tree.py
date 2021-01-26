class nod:
    def __init__(self,character):
        self.character=character
        self.left=None
        self.mid = None
        self.right = None
        self.value=0
class Ternary:
    def __init__(self):
        self.root=None
    def insert(self,key,data):
        self.root=self.insert_item(self.root,key,data,0)
    def insert_item(self,node,key,data,index):
        c=key[index]
        if node==None:
            node=nod(c)
        if c<node.character:
            node.left=self.insert_item(node.left,key,data,index)
        elif c>node.character:
            node.right = self.insert_item(node.right, key, data, index)
        elif index<len(key)-1:
            node.mid=self.insert_item(node.mid,key,data,index+1)
        else:
            node.value=data
        return node
    def get(self,key):
        node=self.get_item(self.root,key,0)
        if node is  None:
            return False
        print( node.value)

    def get_item(self,node,key,index):
        if node==None:
            return None
        c=key[index]
        if c<node.character:
            return self.get_item(node.left,key,index)
        elif c>node.character:
            return self.get_item(node.right,key,index)
        elif index<len(key)-1:
            return self.get_item(node.mid,key,index+1)
        return node

hash=Ternary()
hash.insert("anas",32)
hash.insert("imane",100)
hash.insert("marwa",123)
hash.get("anas")





