def radix_sort(lista):
  n = 0
  for e in lista:
    if len(e) > n:
      n = len(e)
  
  for i in range(0, len(lista)):
    while len(lista[i]) < n:
      lista[i] = "0" + lista[i]
  
  return lista

print(radix_sort(["100","4","45"]))