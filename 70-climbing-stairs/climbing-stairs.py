class Solution(object):
    def climbStairs(self, n):
        #climbStairs(n-1)+climbStairs(n-2)
        #if n =2 then return n
        #if dp != -1, then dp[n]


        dp = [-1]*(n+1)
        return self.solve(n,dp)
    def solve(self,n,dp):
        if dp[n]!= -1:
            return dp[n]
    
        if n <=2:
            return n
        dp[n]=self.solve(n-1,dp)+self.solve(n-2,dp)
        return dp[n]




        