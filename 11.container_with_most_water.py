from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        return height

if __name__ == "__main__":
    solution = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Max area:", solution.maxArea(heights))