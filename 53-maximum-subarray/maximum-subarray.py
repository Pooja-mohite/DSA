class Solution(object):
    def maxSubArray(self, nums):
        """
        n= len(nums)
        maxsum = nums[0]
        for i in range(n):
            currsum = 0
            for j in range(i, n):
                currsum = currsum + nums[j]
                if currsum > maxsum:
                    maxsum = currsum
        return maxsum"""

        # kadane's pattern
        # at first index we got bestending
        # traverse array, take addition( prev answer with currennt )and comapre with (current)compare and return max

        bestending = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            max1 = bestending + nums[i]
            max2 = nums[i]
            bestending = max(max1, max2)
            ans = max(ans,bestending)
        return ans


        
       
                
        
        


                
        