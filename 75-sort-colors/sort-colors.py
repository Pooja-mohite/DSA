class Solution(object):
    def sortColors(self, nums):
        """
        # if condition is not given
        nums.sort()
        """
        #  brute force
        """
        n= len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    """
        n = len(nums)            
        left = 0
        right = n-1
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left = left + 1
        for i in range(n-1,-1,-1):
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right = right - 1
            


       
        