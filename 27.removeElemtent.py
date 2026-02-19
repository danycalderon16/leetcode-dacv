class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1 
    
        while True:
            if i > j:
                break
            if nums[j] == val:
                nums.pop()
                j -= 1 
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                nums.pop()
            i += 1

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([3],3)
    print(r)