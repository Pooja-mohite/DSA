class Solution(object):
    def maxSubArray(self, nums):
        '''
        #brute force
        n= len(nums)
        maxsum = nums[0]
        for i in range(n):
            currsum = 0
            for j in range(i, n):
                currsum = currsum + nums[j]
                if currsum > maxsum:
                    maxsum = currsum
        return maxsum
        '''
        n = len(nums)
        maxsum = nums[0]
        currsum = 0
        for i in range(n):
            currsum = max(nums[i], currsum + nums[i])
            if currsum > maxsum:
                maxsum = currsum
        return maxsum

                
        
        


                
        