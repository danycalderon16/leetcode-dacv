def radix_sort(lista):
  n = 0
  for e in lista:
    if len(e) > n:
      n = len(e)
  
  for i in range(0, len(lista)):
    while len(lista[i]) < n:
      lista[i] = "0" + lista[i]

  for j in range(n-1,-1, -1):
    groups = [ [] for j in range(10)]
    for i in range(len(lista)):
      pos = int(lista[i][j])
      groups[pos].append(lista[i])
    
    lista = [ el for group in groups for el in group ]
  
  return lista

print(radix_sort(["100","4","45"]))