# 
class Vertice:
  def __init__(self, i):
    self.id = i
    self.visitado = False
    self.nivel = -1
    self.vecinos = []

  def agregaVecino(self, v):
    if v not in self.vecinos:
      self.vecinos.append(v)


class Grafica:
  def __init__(self):
    self.vertices = {}

  def agregaVertice(self, v):
    if v not in self.vertices:
      self.vertices[v] = Vertice(v)
  
  def agregarArista(self, a, b):
    if a in self.vertices and b in self.vertices:
      self.vertices[a].agregaVecino(b)
      self.vertices[b].agregaVecino(a)

  def bfs(self, r):
    l = []
    if r in self.vertices:
      cola = [r]
      l.append(r)
      self.vertices[r].visitado = True
      self.vertices[r].nivel = 0

      print("("+str(r)+","+str(self.vertices[r].nivel)+")")

      while len(cola) > 0:
        actual = cola[0]
        cola = cola[1:]

        for v in self.vertices[actual].vecinos:
          if self.vertices[v].visitado == False:
            cola.append(v)
            l.append(v)
            self.vertices[v].visitado = True
            self.vertices[v].nivel = self.vertices[actual].nivel + 1
            print("("+str(v)+","+str(self.vertices[v].nivel)+")" )

    return l

def main():
  g = Grafica()

  l = [0,1,2,3,4,5,6]
  for v in l:
    g.agregaVertice(v)

  l = [1,4,4,3,4,6,3,5,3,2,6,5,5,2]

  for i in range(0, len(l)-1, 2):
    g.agregarArista(l[i], l[i+1])

  # for v in g.vertices:
  #   print(v,g.vertices[v].vecinos)

  print(g.bfs(2))


if __name__ == '__main__':
  main()