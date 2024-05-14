class Solution(object):
    def majorityElement(self, nums):
        elements = {}

        for num in nums:
          if num in elements:
            elements[num] = elements.get(num) + 1
          else:  
            elements[num] = 1

        major = 0
        for key, value in elements.items():
          if value > major:
            major = key
          
        return major

        
if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))