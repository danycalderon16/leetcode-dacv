
class Solution:
    def search(self, nums, target: int) -> int:
      left = 0
      right = len(nums) - 1
      return self.bsr(nums, target, left, right)

    def bsr(self, nums, target:int, left:int, right:int):
      if(left>right):
        return -1
      elif nums[left]==target:
        return left
      elif nums[right]==target:
        return right
      else:
        piv = (left+right) // 2
        middle = nums[piv]
        if(middle==target):
          return piv
        else:
          # check sorted sublist
          if nums[left]<middle:#left sorted, right unsorted
            if target>middle:
              return self.bsr(nums,target, piv+1, right)
            else:
              if target<nums[left]:
                return self.bsr(nums,target, piv+1, right)
              else:
                return self.bsr(nums,target, left, piv-1)
              
          else:#left unsorted, right sorted
            if target<middle:
              return self.bsr(nums,target, left, piv-1)
            else:
              if target<nums[right]:
                return self.bsr(nums,target, piv+1, right)
              else:
                return self.bsr(nums,target, left, piv-1)


if __name__ == "__main__":
  bs = Solution()
  print(bs.search([2,5,6,0,0,1,2],3))
# print(bs.search([0,1,2,3,4,5,6],0))