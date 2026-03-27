
class HashMap:
    
    def __init__(self):
        self.size = 4
        self.map = [ [] for i in range(0,self.size)]
    
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def search(self, key)->bool:
        index = self._hash(key)
        elements = self.map[index]
        if not elements:
            return False
        for el in elements:
            if el[0] == key:
                return True
        return False 
            
    def add(self, key, value):
        index = self._hash(key)
        if self.search(key):
            for el in self.map[index]:
                if el[0] == key:
                    el[1] = value
        else:
            self.map[index].append((key, value))
        
    
    def remove(self, key):
        index = self._hash(key)
        elements = self.map[index]
        if not elements:
            raise KeyError("Key not found")
        for el in elements:
            if el[0] == key:
                elements.remove(el)
                return
        raise KeyError("Key not found")
    
    
    def get(self, key):
        index = self._hash(key)
        elements = self.map[index]
        if not elements:
            raise KeyError("Key not found")
        for el in elements:
            if el[0] == key:
                return el[1]
        raise Exception("Key not found")
    
    
    def display(self):
        print(self.map)
        
    
if __name__ == "__main__":
    
    h = HashMap()
    
    h.add("nombre","Daniel")
    h.add("edad",25)
    h.add("apellido", "Calderon")
    h.add("city","Tepic")
    h.display()
    h.remove("edad")
    h.display()
    
    print(h.get("nombre"))
