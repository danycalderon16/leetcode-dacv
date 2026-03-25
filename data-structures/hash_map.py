
class HashMap:
    
    def __init__(self):
        self.size = 1
        self.map = [ [] for i in range(0,self.size)]
    
    
    def _hash(self, value):
        return hash(value) % self.size
    
    def add(self, value):
        key = self._hash(value)
        if self.map[key] is []:
            self.map[key] = [value]
        else:
            self.map[key].append(value)
    
    def remove(self, value):
        key = self._hash(value)
        elements = self.map[key]
        if elements:
            for el in elements:
                if el == value:
                    elements.remove(el)
                    return
        
    def display(self):
        print(self.map)
if __name__ == "__main__":
    
    h = HashMap()
    h.add("Hola")
    h.add("Mundo")
    h.add("messi")
    h.add("neymar")
    h.display()
    h.remove("neymar")
    h.display()