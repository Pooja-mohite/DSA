class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # BRUTE force =
        """
        m = len(text1)
        n = len(text2)
        def dfs(i,j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1,j+1)
            mskip= dfs(i+1,j)
            nskip= dfs(i, j+1)

            return max(mskip, nskip)
        return dfs(0,0)
            """
            #(DP)=
        m = len(text1)
        n = len(text2)
        dp = [[-1]*n for _ in range(m)]
        def dfs(i,j):
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j]= 1 + dfs(i+1, j+1)
                
            else:
                mskip = dfs(i+1,j)
                nskip = dfs(i , j+1)
                dp[i][j] = max(mskip, nskip)
            return dp[i][j]
        return dfs(0,0)
        