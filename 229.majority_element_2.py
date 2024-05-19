class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        elements = {}
        contition = len(nums) / 3
        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1

        keys = []

        for key, value in elements.items():
            if value > contition:
                keys.append(key)

        return keys


if __name__ == '__main__':
    nums = [3,2,3,2,1,1,3,2,3,2,2]
    print(Solution().majorityElement(nums))