class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        return self.bsMatrix(matrix,0, len(matrix)-1, target)
    
    def bsMatrix(self,matrix, left, right, target):
        if(left>right):
            return False;
        else:
            piv = (right+left)//2
            if(target== matrix[piv][0] or target== matrix[piv][-1]):
                return True
            else:
                if (target> matrix[piv][0] and target < matrix[piv][-1]):
                    return self.bsArray(matrix[piv],0,len(matrix[piv]), target)
                else:
                    if(target<matrix[piv][0]):
                        return self.bsMatrix(matrix,left, piv-1, target)
                    elif target>matrix[piv][-1]:
                        return self.bsMatrix(matrix, piv+1, right, target)

    def bsArray(self,arr, left, right, target):
        if(left>right):
            return False
        else:
            piv = (left + right) //2
            if(arr[piv] == target):
                return True
            else:
                if target < arr[piv]:
                    return self.bsArray(arr, left, piv-1, target)
                else:
                    return self.bsArray(arr, piv+1, right, target)


if __name__ == "__main__":

    sr = Solution()
    res = sr.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],22)
    print(res)