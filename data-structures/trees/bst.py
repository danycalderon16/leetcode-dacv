class Node(object):
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class BST():
    
    def __init__(self):
        self.root = None
    
    def insert(self, value: int):
        if self.root == None:
            self.root = Node(value)
            return
        
        self.insert_rec(self.root,value)
        
    def insert_rec(self,leef:Node, value:int):
        if leef.val > value:
            if not leef.left:
                leef.left = Node(value)
            else:
                self.insert_rec(leef.left, value)
        else:
            if not leef.right:
                leef.right = Node(value)
            else:
                self.insert_rec(leef.right, value)
        
        return
        
        
if __name__ == "__main__":
    tree = BST()
    
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)