import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1

        return self.bs(nums,target, left, right)
    
    def bs(nums:list, target:int,left:int, right:int)-> int:
      if(left>right):
        return -1
      else:
        piv = ((right+left) // 2)
        if(nums[piv] == target):
          return piv
        else:
            if(target<nums[piv]):
              return self.bs(nums, target,left,piv-1)
            else:
              return self.bs(nums,target, piv+1, right)

if __name__ == "__main__":

  sr = Solution()

  res = sr.searchRange([5,7,7,8,8,102],8)

  print(res)
  # 0 1 2 3 4 5 | 6 7 8 | 9 10 |