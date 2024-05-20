class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        results = ""

        while columnNumber > 0:
          results += (chr((columnNumber-1)%26+65))
          columnNumber = (columnNumber-1) // 26; 
        
        return (results[::-1])
        

if __name__ == "__main__":
    print(Solution().convertToTitle(72332332330231))