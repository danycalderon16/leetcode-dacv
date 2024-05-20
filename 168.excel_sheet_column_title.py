class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        results = []

        while columnNumber > 0:
          results.append(chr((columnNumber-1)%26+65))
          columnNumber = (columnNumber-1) // 26; 
        
        results.reverse()

        return "".join(results)
        

if __name__ == "__main__":
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(2))
    print(Solution().convertToTitle(10))
    print(Solution().convertToTitle(701))