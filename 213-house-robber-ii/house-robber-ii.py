class Solution(object):
    def rob(self, nums):
        #brute force
        #helper recursion
        """
        def helper(arr, i):
            if i >= len(arr):
                return 0

            #take current
            take = arr[i] + helper(arr, i+2)

            #skip current
            skip = helper(arr, i+1)

            return max(take, skip)

        n = len(nums)

        if n == 1:
            return nums[0]

        # case1:exclude last house
        case1 = helper(nums[0:n-1], 0)

        #case2:exclude first house
        case2 = helper(nums[1:n], 0)

        return max(case1, case2)
        """

        #optimized(DP)  
        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            dp = [0]*n

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                take = arr[i] + dp[i-2]
                skip = dp[i-1]

                dp[i] = max(take, skip)

            return dp[n-1]

        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = helper(nums[0:n-1]) 
        case2 = helper(nums[1:n])

        return max(case1, case2)  