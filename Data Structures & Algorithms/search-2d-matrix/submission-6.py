class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        row = 0
        while row < len(matrix):
            a,b = 0,len(matrix[0])-1
            while a<=b:
                mid = (a+b)//2
                if matrix[row][mid] < target:
                    a+=1
                elif matrix[row][mid] > target:
                    b-=1
                else:
                    return True
            row+=1
        return False

        
        