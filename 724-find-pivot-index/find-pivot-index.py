class Solution(object):
    def pivotIndex(self, nums):
        # left side sum == right side sum retun idex else retun -1

        """n = len(nums)
        for i in range(n):
            lsum = 0
            rsum =0
            for j in range(i):
                lsum = lsum + nums[j]
            for j in range(i+1, n):
                rsum =  rsum + nums[j]
            if lsum == rsum:
                return i
        return -1"""
        # prefix
        n = len(nums)
        left = 0
        ssum = sum(nums)
        for i in range(n):
            if i > 0:
                left = left + nums[i-1]
            right = ssum - nums[i] - left
            if left == right:
                return i
        return -1
        
                
                

        
        