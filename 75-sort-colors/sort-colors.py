class Solution(object):
    def sortColors(self, nums):
        """
        # if condition is not given
        nums.sort()
        """
        n= len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

       
        