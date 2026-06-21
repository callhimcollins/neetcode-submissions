class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while top <= bottom and left <= right:
            # Left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # top to bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # bottom to top
            if left <= right:
                for row in range(bottom, top -1, -1):
                    res.append(matrix[row][left])
                left += 1
        
        return res