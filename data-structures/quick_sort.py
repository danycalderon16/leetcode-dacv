class Solution:
  def quick_sort(self,list):
    if len(list) <=1:
      return list

    piv = list[len(list)//2]
    lista1 = [x for x in list if x < piv ]
    middle = [x for x in list if x == piv]
    lista2 = [x for x in list if x > piv ]

    lista1 = self.quick_sort(lista1)
    lista2 = self.quick_sort(lista2)

    return lista1 + middle +lista2


if __name__ == "__main__":
  list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(Solution().quick_sort(list))
  list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
  print(Solution().quick_sort(list))
  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(Solution().quick_sort(list))
  list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  print(Solution().quick_sort(list))
  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  print(Solution().quick_sort(list))