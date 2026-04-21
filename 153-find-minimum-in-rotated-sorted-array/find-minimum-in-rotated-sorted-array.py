class Solution(object):
    def findMin(self, nums):


        #brute force
        """
        minimum = nums[0]
        for i in range(len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
        return minimum 
        """
        #binary search
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]

        