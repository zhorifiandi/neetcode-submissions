class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_up, row_down = 0, len(matrix) - 1

        while row_up <= row_down:
            row_mid = (row_up + row_down) // 2
            if matrix[row_mid][0] == target or target == matrix[row_mid][-1]:
                return True
            
            if matrix[row_mid][0] < target < matrix[row_mid][-1]:
                col_left, col_right = 0, len(matrix[0]) - 1
                while col_left < col_right:
                    col_mid = (col_left + col_right) // 2
                    if target == matrix[row_mid][col_mid]:
                        return True
                    elif target < matrix[row_mid][col_mid]:
                        col_right = col_mid - 1
                    else:
                        col_left = col_mid + 1
                
                return False
            elif target < matrix[row_mid][0]:
                row_down = row_mid - 1
            else:
                row_up = row_mid + 1
        
        return False