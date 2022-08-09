class Solution:
    #def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target):
        rows = len(matrix[0])
        cols = len(matrix)
        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m // rows][m % rows] > target:
                r = m - 1
            elif matrix[m // rows][m % rows] < target:
                l = m + 1
            else:
                return True
        return False
