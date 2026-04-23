class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            #boundary check
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return

            if grid[i][j] == "0":
                return

            #mark visited
            grid[i][j] = "0"

            #visit all 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count = count + 1
        return count
        