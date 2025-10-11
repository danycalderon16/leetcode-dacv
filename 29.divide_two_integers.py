class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        signs = [0,0]

        if dividend < 0:
          dividend = -dividend
          signs[0] = 1
            
        if divisor < 0:
          divisor = -divisor
          signs[1] = 1
        
        quocient = 0
          
        while True:
          if dividend - divisor >= 0:
            dividend -= divisor
            quocient += 1
          else:
            break
        
        if signs[0] != signs[1]:
          quocient = -quocient
        
        return min(max(-2147483648, quocient), 2147483647)
        
if __name__ == '__main__':
    s = Solution()
    print(s.divide(7, -3))  
    print(s.divide(-7, -3))  
    print(s.divide(7, 3))  