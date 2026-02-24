from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0: 
            return len(nums)
        
        limit = len(nums)         
        i = 1
        j = 1
          

        while j < limit :
            if nums[j] != nums[i - 1]:
                j +=1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
                

        return len(nums)
    

if __name__ == "__main__":
    s = Solution()
    r = s.removeDuplicates([1,1,2,2,2,2,3,3,4])
    
    print(r)