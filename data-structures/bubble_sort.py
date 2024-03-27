

class Solution:
  def bubble_sort(self,list):
    n = len(list)

    for i in range(1,n):
      for j in range (0, n-1):
        if list[j] > list[j+1]:
          aux = list[j+1]
          list[j+1] = list[j]
          list[j] = aux 

    return list


if __name__ == "__main__":
  list = [11, 2, 33, 9, 15]
  Solution().bubble_sort(list)
  print(list)