def convCad(cad):
  output = ""

  for l in cad:
    output += str(ord(l))

  return int(output)


def hashN(cad, m):
  i = convCad(cad)

  return int(m*(i*0.0000000000000021345653%1))


def agregar(cad, ht, m):
  res = hashN(cad, m)
  ht[res].append(cad)


def search(cad, ht, m):
  res = hashN(cad, m)
  for i in ht[res]:
    if i == cad:
      return True
  return False


if __name__ == "__main__":
  m = 19
  ht = [[] for i in range(m)]

  agregar("hola", ht, m)
  agregar("adios", ht, m)
  agregar("hola", ht, m)

  print(search("hola", ht, m))
  print(search("adios", ht, m))
  print(search("hol", ht, m))
  print(search("holaa", ht, m))