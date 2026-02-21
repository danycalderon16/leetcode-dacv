from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # li = len(nums) - 1
        # piv = 0 

        # while piv < li:
        #     if nums[piv] == nums[piv + 1]:
        #         nums.pop(piv + 1)
        #         li -= 1
        #     else:
        #         piv += 1


        # return len(nums)
        unique_values = set([])
        for n in nums:
            unique_values.add(n)


        return len(unique_values)
    

if __name__ == "__main__":
    s = Solution()
    r = s.removeDuplicates([1,1,2])
    
    print(r)