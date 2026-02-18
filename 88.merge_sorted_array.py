class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n:int) -> list:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        piv = m + n - 1
        m= m-1
        n = n-1
        
        while True:
            if n == -1:
                break
            elif m == -1:
                nums1[piv] = nums2[n]
                n -= 1
            elif nums1[m] >= nums2[n]:
                nums1[piv] = nums1[m]
                m -= 1
            else:
                nums1[piv] = nums2[n]
                n -= 1
            piv -= 1
        return nums1
    
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,0]
    nums2 = [1]
    m = 1
    n = 1
    print(solution.merge(nums1,m,nums2,n))