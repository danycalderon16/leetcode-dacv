def binary_search(nums:list, target:int )->int:
  left = 0
  right = len(nums)-1

  return bs(nums,target, left, right)

def bs(nums:list, target:int,left:int, right:int)-> int:
  if(left>right):
    return -1
  else:
    piv = ((right+left) // 2)
    if(nums[piv] == target):
      return piv
    else:
        if(target<nums[piv]):
          return bs(nums, target,left,piv-1)
        else:
          return bs(nums,target, piv+1, right)


if __name__ == "__main__":
  res = binary_search([-1,0,3,5,9,12],2)

  print(res)
  # 0 1 2 3 4 5 | 6 7 8 | 9 10 |