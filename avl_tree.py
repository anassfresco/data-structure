class nod:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.height=0

class avl:
    def __init__(self):
        self.tree=None
    def calcule_height(self,node):
        if node is None:
            return -1
        else:
            return node.height
    def calcule_balance(self,node):
        if node is None :
            return 0
        else:
            return self.calcule_height(node.left)-self.calcule_height(node.left)
    def right_rotate(self,node):
        print("rotate to right")
        left_node=node.left
        t=left_node.right
        left_node.right=node
        node.left=t
        node.height=max(self.calcule_height(node.right),self.calcule_height(node.left))+1
        left_node.height=max(self.calcule_height(left_node.right),self.calcule_height(left_node.left))+1
        return left_node
    def left_rotate(self,node):
        print("rotate to left")
        right_node=node.right
        t=right_node.right
        right_node.right=node
        node.right=t
        node.height=max(self.calcule_height(node.right),self.calcule_height(node.left))+1
        right_node.height=max(self.calcule_height(right_node.right),self.calcule_height(right_node.left))+1
        return right_node



    def insert(self,data):
        self.tree=self.insert_node(self.tree,data)
    def insert_node(self,node,data):
        new_node=nod(data)
        if node is None:
            return new_node
        if data>node.data:
            node.right=self.insert_node(node.right,data)
        if data<node.data:
            node.left=self.insert_node(node.left,data)

        node.height=max(self.calcule_height(node.right),self.calcule_height(node.left))+1
        return self.check(node,data)
    def check(self,node,data):
        balance=self.calcule_balance(node)
        #case 1 right rotation
        if balance>1 and  data<node.left.data:
            print("right rotation")
            return self.right_rotate(node)
        elif balance<-1 and data>node.right.data:
            print("its a left rotation")
            return self.left_rotate(node)
        elif  balance>1 and data>node.left.data:
            print("is a left right rotation")
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance<-1 and data<node.right:
            print("its a right left rotation")
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        return node
    def pre_order(self):
        if self.tree is not None:
             self.preoreder2(self.tree)
    def preoreder2(self,node):
        if node.left:

             self.preoreder2(node.left)
        print(node.data)
        if node.right:
            self.preoreder2(node.right)
    def remove(self,data):
        if self.tree:
            self.tree=self.remove_node(self.tree,data)
    def remove_node(self,node,data):
        if node is None:
            return node
        if data<node.data:
            node.left=self.remove_node(node.left,data)
        elif data>node.data:
            node.right=self.remove_node(node.right,data)
        else:
            if not node.left and not node.right:
                print("single node without children ")
                del node
                return None
            if node.left is None:
                print(" node with right children")
                right_chidren=node.right
                del node
                return right_chidren
            elif node.right is None:
                print("node has a left child")
                left_children=node.left
                del node
                return left_children
            print("node with 2 childrens ")
            Predecessor_node=self.get_Predecessor(node.left)
            node.data=Predecessor_node.data
            node.left=self.remove_node(node.left,Predecessor_node.data)
            node.height=max(self.calcule_height(node.right),self.calcule_height(node.left))+1
        if not node:
            return node
        node.height=max(self.calcule_height(node.right),self.calcule_height(node.left))+1
        balance=self.calcule_balance(node)
        if balance>=1 and self.calcule_balance(node.left)>0:
            print("right rotation")
            return self.right_rotate(node)
        if balance<-1 and self.calcule_balance(node.right)<0:
            print("its a left rotation")
            return self.left_rotate(node)
        if  balance>1 and self.calcule_balance(node.left)<0:
            print("is a left right rotation")
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance<-1 and self.calcule_balance(node.right)>0:
            print("its a right left rotation")
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        return node







    def get_Predecessor(self,node):
        if node.right:
            return self.get_Predecessor(node.right)
        return node

avl=avl()
avl.insert(1)
avl.insert(4)
avl.insert(75)
avl.insert(621)
avl.insert(8)
avl.insert(834)
avl.insert(83)
avl.insert(38)
avl.insert(85)
avl.remove(120)

avl.pre_order()






