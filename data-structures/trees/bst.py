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
        
    def insert_rec(self,leaf:Node, value:int):
        if value == leaf.val: return
        if leaf.val > value:
            if not leaf.left:
                leaf.left = Node(value)
            else:
                self.insert_rec(leaf.left, value)
        else:
            if not leaf.right:
                leaf.right = Node(value)
            else:
                self.insert_rec(leaf.right, value)
        
        return
    def print_tree(self, type="inOrden"):
        if type == "inOrden":
            self.in_orden(self.root)
        if type == "postOrden":
            self.post_orden(self.root)
        if type == "preOrden":
            self.pre_orden(self.root)
        
    def in_orden(self, root:Node):
        if not root: return
        self.in_orden(root.left)
        print(root.val)
        self.in_orden(root.right)
        
    def post_orden(self, root):
        if not root: return
        self.post_orden(root.left)
        self.post_orden(root.right)
        print(root.val)
    
    def pre_orden(self, root:Node):
        if not root: return
        print(root.val)
        self.pre_orden(root.left)
        self.pre_orden(root.right)
        
if __name__ == "__main__":
    tree = BST()
    
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.print_tree("preOrden")