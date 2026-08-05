class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])

        def expand(i, j):
            withinRange = 0 <= i < m and 0 <= j < n
            if not withinRange:
                return
            
            if grid[i][j] != "1":
                return
            
            grid[i][j] = "-1"
            for di, dj in [(0,1), (0,-1), (1,0), (-1, 0)]:
                expand(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    expand(i, j)
                    islands += 1
        
        return islands