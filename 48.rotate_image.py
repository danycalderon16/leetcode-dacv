
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        j = len(matrix[0])
        
        for i in range(0,n):
            for j in range(i+1,n):
                temp= matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp 
                
        for i in range(0,n):
            left = 0
            right = n - 1 
            while left<right:
                temp = matrix[i][left]
                matrix[i][left]=matrix[i][right]
                matrix[i][right]=temp
                left+=1
                right-=1
        
        return (matrix)
        

if __name__ == "__main__":
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
    print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(s.rotate([[1]]))  # [[1]]
    print(s.rotate([[1,2],[3,4]]))  # [[3,1],[4,2]]