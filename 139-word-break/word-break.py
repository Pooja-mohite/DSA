class Solution(object):
    def wordBreak(self, s, wordDict):
        #brutr force
        """
        n = len(s)
        def helper(start):
            if start == n:
                return True
       
            for j in range(start+1, n+1):
                word = s[start:j]
                if word in wordDict:
                    if helper(j):
                       return True
                
            return False
        return helper(0)
        """
        #DP
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1,-1,-1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[j] == True:
                    dp[i] = True
            
                
        return dp[False]



            


        
        