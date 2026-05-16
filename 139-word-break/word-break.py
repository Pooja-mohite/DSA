class Solution(object):
    def wordBreak(self, s, wordDict):
        '''
        n = len(s)
        def check(start):
            if start == n:
                return True
            for j in range(start+1, n+1):
                word = s[start:j]
                if word in wordDict:
                    if check(j):
                        return True
            return False
        return check(0)
        '''
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1,-1,-1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[j] == True:
                    dp[i] = True
        return dp[0]



                





       
          
        