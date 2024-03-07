class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = set()
        a = [1,2]
        b = [2,1]
        triplets.add(a.sort())
        triplets.add(b.sort())
        triplets.add(1)
        return  triplets


if __name__ == "__main__":
    solution = Solution()
    heights = [-1,0,1,2,-1,4]
    print("Triplets: ", solution.threeSum(heights))