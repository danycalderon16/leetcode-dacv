class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for i in digits:
            num += str(i)

        num = int(num) + 1   
        num = str(num)

        res = []
        for c in num:
            res.append(int(c))

        return res

        
if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))