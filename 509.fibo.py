
class Solution(object):

    def fib(self, n: int) -> int:
      if (n == 0):
        return n
      if (n==1) or (n==2):
        return 1

      nums = [1,1]
      # fibo = 0
      for i in range(3, n+1):
        fibo = nums[0] + nums[1]
        nums[0] = nums[1]
        nums[1] = fibo
      
      return nums[1]
      
    
if __name__ == "__main__":

  res = Solution().fib(10)

  print(res)  