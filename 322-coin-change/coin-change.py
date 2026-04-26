class Solution(object):
    def coinChange(self, coins, amount):
        #brute force
        """
        def solve(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            ans = -1
            for coin in coins:
                res = solve(rem-coin)
                if res != -1:
                    if ans == -1:
                        ans = res + 1
                    else:
                        ans = min(ans, res+1)
            return ans
        return solve(amount)
        """
        #optimized(DP)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        i = 1
        while i <= amount:
            j = 0
            while j < len(coins):
                coin = coins[j]
                if i - coin >= 0 and dp[i - coin] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
                j = j+1
            i = i+1
        return dp[amount]
            


                

        
    
        