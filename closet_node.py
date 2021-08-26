    def closest_point(self,target):
        max=sys.maxsize
        target2=None
        actual_node=self.tree
        while actual_node is not None and actual_node.data!=target:

            target2, max = self.comparaison(actual_node, target, max,target2)
            if target>actual_node.data:
                actual_node=actual_node.right_node

            else:
                actual_node=actual_node.left_node
            print(actual_node.data)
        if actual_node.data==target:
            return target
        else:

            return target2
    def comparaison(self,node,target,max,precedente):
        if abs(node.data - target) < max:
            target1 = node.data
            max1 = node.data - target
            return  target1,max1
        else:
            return precedente,max
