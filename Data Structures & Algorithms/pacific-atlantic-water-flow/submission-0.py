class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visited, prevHeight):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or heights[r][c] < prevHeight:
                return

            visited.add((r, c))
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, visited, heights[r][c])

        # Do the left and right borders
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        # Do the top and bottom borders
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        # Do intersection of both sets
        return [list(point) for point in pac & atl]


                   