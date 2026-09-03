class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        columns = len(matrix[0])
        
        left = 0
        right = rows * columns - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // columns
            col = mid % columns
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
