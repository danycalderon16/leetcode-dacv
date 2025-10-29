class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 2
        while True:
            if x-1 >= n:
                return x-1
            x = x * 2
        