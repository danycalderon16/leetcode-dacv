class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        triplets = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1 
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    triplets.add(triplet) 
                    j += 1
                    k -= 1
                elif sum < 0:
                    j = j+1
                else:
                    k = k - 1

        output = list(triplet)
        return  output


if __name__ == "__main__":
    solution = Solution()
    heights = [-1,0,1,2,-1,-4]
    print("Triplets: ", solution.threeSum(heights))