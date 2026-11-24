class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = row + dr, col + dc
                    dfs(nr, nc)
                return 1
            return 0
        
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    total += 1
        return total
