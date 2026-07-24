class Solution(object):
    def fib(self, n):
        """
        if n <2:
            return n
        return self.fib(n-1)+ self.fib(n-2)
        """
        """
        self.dp=[-1]*(n+1)
        return self.find(n)
    def find(self,n):
        if self.dp[n] != -1:
            return self.dp[n]
        if n < 2:
            return n
        self.dp[n] = self.find(n-1)+self.find(n-2)
        return self.dp[n]"""

        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        

        
        
       
        