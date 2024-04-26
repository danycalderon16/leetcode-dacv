class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int 
        """
        if len(needle)> len(haystack) : return - 1
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
              j += 1
            if j == len(needle):
              return i
        return -1
if __name__ == '__main__':
  s = Solution()
  # s.strStr("hello", "ll")
  print(s.strStr("hello", "ll"))