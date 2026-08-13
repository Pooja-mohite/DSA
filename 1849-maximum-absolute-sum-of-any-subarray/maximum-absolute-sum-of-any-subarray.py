class Solution(object):
    def maxAbsoluteSum(self, nums):
        # [1,-3,2,3,-4] =
        """n = len(nums)
        maxsum = nums[0]
        for i in range(n):
            ssum = 0
            for j in range(i,n):
                ssum = (ssum + nums[j])
                maxsum = max(maxsum,abs(ssum))
        return maxsum"""

        # find subarry, then find sum, maxsum and minsum, and return maxsum form them

        n = len(nums)
        maxend = 0
        minend = 0
        maxendsum = 0
        minendsum = 0
        for i in range(n):
            maxend = max(nums[i],nums[i] + maxend)
            maxendsum = max(maxend,maxendsum)
            minend = min(nums[i],nums[i] + minend)
            minendsum = min(minend, minendsum)
            ans = max(abs(maxendsum),abs(minendsum))
        return ans



       
        