class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

class Stack:
    
    def __init__(self):
        self.top = None
    
    def push(self, node:Node):
        if self.top == None:
            self.top = node
        else:
            piv = self.top
            self.top = node
            self.top.prev = piv
    
    def is_empty(self)->bool:
        return self.top is None
    
    def peek(self)->Node:
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.top
    
    def pop(self)->Node:
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            piv = self.top
            self.top = self.top.prev
            return piv
            
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
    stack.pop()
    stack.pop()
    print(stack.print())
    stack.pop()
    stack.pop()