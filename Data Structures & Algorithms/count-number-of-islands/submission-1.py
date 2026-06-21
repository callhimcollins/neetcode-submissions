class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        island = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    drow, dcol = row + dr, col + dc
                    if drow in range(rows) and dcol in range(cols) and grid[drow][dcol] == '1' and (drow, dcol) not in seen:
                        q.append((drow, dcol))
                        seen.add((drow, dcol))
                        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in seen:
                    bfs(row, col)
                    island += 1
        return island
