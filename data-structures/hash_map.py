import math

class HashMap:
    
    def __init__(self):
        self.map = []
    
    def add(self, value):
        key = math.ceil(value*math.pow(value, 2)*math.pi % 40)
        print(key)
        
if __name__ == "__main__":
    h = HashMap()
    for i in range(0,100):
        h.add(i)    