class Solution(object):
    def uniquePaths(self, m, n):
        '''
        #brute force
        def dfs(i,j):
            if i > m or j>n:
                return 0
            if i == m - 1 and j == n-1:
                return 1
            right = dfs(i, j+1)
            down = dfs(i+1,j)
            return right + down
        return dfs(0,0)
        '''    
        dp = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if i >= m or j>= n:
                return 0
            if i == m - 1 and j== n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            right = dfs(i, j+1)
            down = dfs(i+1, j)
            dp[i][j] = right + down
            return dp[i][j]
        return dfs(0,0)





        