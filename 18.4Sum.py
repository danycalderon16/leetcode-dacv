class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums) 
        nums.sort()

        cuadruplet = set()

        output = []

        for i in range(n):
          for j in range(i+1, n):
            k = j + 1
            l = n - 1

            while k < l:
              sum = nums[i] + nums[j] + nums[k] + nums[l]

              if sum == target:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                cuadruplet.add(tuple(temp))
                k += 1
                l -= 1
              elif sum < target:
                k += 1
              else:
                l -= 1
              
        output = list(cuadruplet)
        return output

if __name__ == "__main__":
    bs = Solution()
    print(bs.fourSum([1,0,-1,0,-2,2], 0))
#   print(bs.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18],0))
