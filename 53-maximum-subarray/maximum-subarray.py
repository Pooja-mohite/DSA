class Solution(object):
    def maxSubArray(self, nums):
        #burte force
        '''
        n=len(nums)
        max_sum = nums[0]
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum = current_sum + nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
        '''
        #optimized
        n = len(nums)
        max_sum = nums[0]
        current_sum = 0
        for i in range(n):
            current_sum = max(nums[i], current_sum + nums[i])
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum



      





                
        