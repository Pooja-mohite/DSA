class Solution(object):
    def climbStairs(self, n):
        #climbStairs(n-1)+climbStairs(n-2)
        #if n =2 then return n
        #if dp != -1, then dp[n]


        """dp = [-1]*(n+1)
        return self.solve(n,dp)
    def solve(self,n,dp):
        if dp[n]!= -1:
            return dp[n]
    
        if n <=2:
            return n
        dp[n]=self.solve(n-1,dp)+self.solve(n-2,dp)
        return dp[n]"""

# want to reach nth stairs
# 1 step = (n-1)stairs
# 2 step = (n-2)stairs
# 0 stair = 1 way = already reached
# 1 stair = another way = 1 possible way
#add two ways
        if n== 0 or n== 1:
            return n
        dp = [1]*(n+1)
        dp[1]= 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]







        