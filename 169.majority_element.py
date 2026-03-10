class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}
        major = [0,0]

        for num in nums:
            if num in elements:
                elements[num] = elements.get(num) + 1
            else:  
                elements[num] = 1
            if elements.get(num) > major[1]:
                major[0] = num  
                major[1] = elements.get(num)
        
        return major[0]
        
if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([6,5,5]))