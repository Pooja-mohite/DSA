class Solution(object):
    def fib(self, n):
        """
        if n <2:
            return n
        return self.fib(n-1)+ self.fib(n-2)
        """

        self.dp=[-1]*(n+1)
        return self.find(n)
    def find(self,n):
        if self.dp[n] != -1:
            return self.dp[n]
        if n < 2:
            return n
        self.dp[n] = self.find(n-1)+self.find(n-2)
        return self.dp[n]
        

        
        
       
        