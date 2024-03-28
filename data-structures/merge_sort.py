class Solution:
  def merge_sort(self,list):
    if len(list) == 1:
      return list
    
    l_left = list[:len(list)//2]
    l_rigth = list[len(list)//2:]

    l_left = self.merge_sort(l_left)    
    l_rigth = self.merge_sort(l_rigth)    

    return self.merge(l_left, l_rigth)

  def merge(self, l_left, l_rigth):
    list = []
    while len(l_left)>0 and len(l_rigth)>0:
      if l_left[0] < l_rigth[0]:
        list.append(l_left[0])
        l_left = l_left[1:]
      else:
        list.append(l_rigth[0])
        l_rigth = l_rigth[1:]

    if len(l_left) >0:
      list = list + l_left

    if len(l_rigth) >0:
      list = list + l_rigth
    
    return list


if __name__ == "__main__":
  list = [9,3,2,1,45]
  res = Solution().merge_sort(list)
  print(res)