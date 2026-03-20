class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self)->bool:
        return self.head is None
    
    def enqueue(self, node:Node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def dequeue(self)->Node:
        if self.is_empty():
            raise Exception("Queue empty")
        piv = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return piv
    
    def display(self):
        piv = self.head
        elements = []
        while piv != None:
            elements.append(piv.val)
            piv = piv.next
        print(elements)
        
        
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(Node(2))
    queue.enqueue(Node(3))
    print(queue.dequeue().val)
    queue.enqueue(Node(1))
    queue.display()
    print(queue.dequeue().val)
    print(queue.dequeue().val)
    print(queue.dequeue().val)
    queue.display()