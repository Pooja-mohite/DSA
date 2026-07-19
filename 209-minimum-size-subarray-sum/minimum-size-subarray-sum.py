class Solution(object):
    def minSubArrayLen(self, target, nums):
        # brute force
        """n = len(nums)
        min_len = float("inf")
        for i in range(n):
            summ = 0
            for j in range(i,n):
                summ = summ + nums[j]
                if summ >= target:
                    leng = j -i +1
                    if leng < min_len:
                        min_len = leng
                
            if min_len == float("inf"):
                return 0
        
        return min_len"""

        left = 0
        right = 0
        n = len(nums)
        min_len = float("inf")
        summ = 0
        while right<n:
            summ = summ + nums[right]
            while summ >= target:
                leng = right - left + 1
                if leng < min_len:
                    min_len = leng
                summ = summ - nums[left]
                left = left +1
            right = right + 1
        if min_len == float("inf"):
            return 0
        return min_len

             



       