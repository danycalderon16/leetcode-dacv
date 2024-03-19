class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        return self.bs(matrix, left, right, target)

    def bs(self, matrix, left, right, target):
        if(left>right):
            return False
        else:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid,len(matrix[0]))

            if matrix[mid_row][mid_col] == target:
                return True
            else:
                if target < matrix[mid_row][mid_col] :
                    return self.bs(matrix, left, mid-1, target)
                else:
                    return self.bs(matrix, mid+1, right, target)


if __name__ == "__main__":

    sr = Solution()
    res = sr.searchMatrix([
        [1 ,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]],13)
    print(res)