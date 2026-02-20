class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = len(nums) - 1 
    
        while i <= j:
            if nums[j] == val:
                nums.pop()
                j -= 1 
            elif nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                nums.pop()
            else:
                i += 1

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([3,2,2,3],3)
    print(r)