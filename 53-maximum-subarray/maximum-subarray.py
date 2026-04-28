class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brue force
        """
        n = len(nums)
        maximumsum = nums[0] 
        for i in range(n):
            currentsum = 0
            for j in range(i, n):
                currentsum = currentsum + nums[j]
                if currentsum > maximumsum:
                    maximumsum = currentsum
        return maximumsum
        """
        #Greedy
        n = len(nums)
        maximumsum = nums[0]
        currentsum = 0
        for i in range(n):
            currentsum = max(nums[i], currentsum + nums[i])
            if currentsum > maximumsum:
                maximumsum = currentsum
        return maximumsum





                
        