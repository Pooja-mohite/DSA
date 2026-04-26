class Solution(object):
    def numDecodings(self, s):
        #brute force
        """
        def decode(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = decode(i+1)

            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                ways = ways + decode(i+2)
            return ways
        return decode(0)
        """
        #optimized(DP)
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            #if starts with 0-> invalid
            if s[i] == '0':
                dp[i] = 0
            else:
                #for 1 digit
                dp[i] = dp[i+1]

                #for 2 digits
                if i+1 < n and int(s[i:i+2]) <= 26:
                    dp[i] = dp[i] + dp[i+2]
        return dp[0]

        


            
        
        