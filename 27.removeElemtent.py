class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        
        for i in nums:
          if i != val:
            nums[k] = i
            k += 1

        return k

if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([3,2,2,3],3)
    print(r)