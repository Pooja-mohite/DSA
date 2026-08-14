class Solution(object):
    def maxSubarraySumCircular(self, nums):
        # find subarray 
        # take sum of each and return max sum
        # but array is circular, so we need to find circular index 
        # next element = i+1 % n = [1, -2,3, -2]
        #                           0   1  2  3
        # i = 0, i+1 % n = 0 , 0+1 % 4= 1 goes to next index (-2)
        #and previous elemnt= (i-1+n) % n , i = 2 , 0-1 % 4 = -1 which is wrong so need to add n 0-1+4 % 4 = 3%4 = 3
        """n = len(nums)
        ans = nums[0]
        for i in range(n):
            ssum =0
            for j in range(1,n+1):
                index = (i-j+1)% n
                ssum = ssum + nums[index]  
                ans = max(ssum, ans)
        return ans"""

        # kadanes algo
        # maxsum find, then find minsum 
        # circularsum = totalsum - minsum and then find max
        # if number is negative then find maxsum

        n = len(nums)
        total = sum(nums)
        maxEnding = nums[0]
        maxSum = nums[0]
        minEnding = nums[0]
        minSum = nums[0]
        for i in range(1, n):
            maxEnding = max(maxEnding + nums[i], nums[i])
            maxSum = max(maxSum, maxEnding)
            minEnding = min(minEnding + nums[i], nums[i])
            minSum = min(minSum, minEnding)
        if maxSum < 0:
            return maxSum
        circularSum = total - minSum
        return max(maxSum, circularSum)

        


    
        