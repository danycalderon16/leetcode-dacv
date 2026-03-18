class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

class Stack:
    
    def __init__(self, node:Node):
        self.top = node
    
    def push(self, node:Node):
        if self.top == None:
            self.top = node
        else:
            piv = self.top
            self.top = node
            self.top.prev = piv
            
    def print(self):
        stack = []
        current = self.top
        while current != None:
            stack.append(current.val)
            current = current.prev
        return stack   
            
if __name__ == "__main__":
    stack = Stack(Node(1))
    stack.push(Node(2))
    stack.push(Node(3))
    print(stack.print())