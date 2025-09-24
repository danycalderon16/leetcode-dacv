import re

class Solution:
    def isPalindrome(self, s: str) -> str:
        s = s.lower()
        cleaned = re.sub(r'[^a-z0-9]','',s)
        
        # for i in range(len(cleaned)):
        #     if cleaned[i] != cleaned[-(i+1)]:
        #         return False
            
        return cleaned == cleaned[::-1]
        
if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(s))