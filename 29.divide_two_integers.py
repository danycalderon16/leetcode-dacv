class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        negaviteDivisor = divisor < 0 
        if negaviteDivisor:
          divisor *= -1
        
        negaviteDivident = dividend < 0
        if negaviteDivident:
          dividend *= -1

        quotient = 0
        
        while dividend > 0:
          dividend -= divisor 
          if dividend < 0:
            continue
          quotient += 1

        if negaviteDivident and negaviteDivisor or (not negaviteDivident) and (not negaviteDivisor):
          return quotient

        if negaviteDivident or negaviteDivisor:
          return quotient * (-1)

if __name__ == '__main__':
    s = Solution()
    print(s.divide(7, -3))  
    print(s.divide(-7, -3))  
    print(s.divide(7, 3))  