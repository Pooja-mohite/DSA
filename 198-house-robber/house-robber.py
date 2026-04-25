class Solution(object):
    def rob(self, nums):
        #brute force
        """"
        def houserobber(i):

            if i >= len(nums):
                return 0
            #take current house
            take = nums[i] + houserobber(i+2)

            #skip current house
            skip = houserobber(i+1)

            return max(take, skip)
        return houserobber(0)
        """
        #optimized(DP)
        n = len(nums)
        if n==1:
            return nums[0]

        #dp array
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        #build dp
        for i in range(2, n):
            take = nums[i] + dp[i-2]
            skip = dp[i-1]

            dp[i] = max(take, skip)

        return dp[n-1]
        