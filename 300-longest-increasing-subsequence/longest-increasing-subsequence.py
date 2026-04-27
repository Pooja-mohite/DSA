class Solution(object):
    def lengthOfLIS(self, nums):
        # brute force:
        """
        n = len(nums)
        
        def helper(i, prev):
            if i == n:
                return 0
            #skip current no.
            skip = helper(i+1, prev)
            take = 0
            #take current no.
            if prev is None or nums[i] > prev:
                take = helper(i+1, nums[i]) + 1
            longest = max(take, skip)
            return longest
        return helper(0,None)
        """
        #optimized(DP)=
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                   
        return max(dp)
         

        
            


    
        
        