class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        

        def dfs(row, col):
            if (row < 0 or row >= ROWS) or (col < 0 or col >= COLS) or (grid[row][col] != 1) or (row, col) in seen:
                return 0
            seen.add((row, col))
            return 1 + dfs(row, col + 1) + dfs(row, col - 1) + dfs(row + 1, col) + dfs(row - 1, col) 
        
        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        
        return area