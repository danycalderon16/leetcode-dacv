class Solution:
    def titleToNumber(self, ct: str) -> int:
        # ct = ct[::-1]
        acc = 0
        for i in ct:
            acc = acc*26 + (ord(i) -64)
            
        return acc
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A")) # 1
    print(s.titleToNumber("AB"))  # 28
    print(s.titleToNumber("ZY") ) # 701
    print(s.titleToNumber("FXSHRXW"))  # 2147483647