class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self)->bool:
        return self.head in None
    
    def enqueue(self, node:Node):
        if self.is_empty():
            self.head = node
            self.tail = node
    
    def print(self):
        piv = self.head
        elements = []
        while piv != None:
            elements.append(piv.val)
            piv = piv.prev
            
        print(elements)
        
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(Node(2))
    queue.enqueue(Node(3))
    queue.print()