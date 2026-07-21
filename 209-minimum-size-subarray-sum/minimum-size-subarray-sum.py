class Solution(object):
    def minSubArrayLen(self, target, nums):

        """
        n = len(nums)
        min_len = float("inf")
        for i in range(n):
            suum = 0
            for j in range(i,n):
                suum = suum +nums[j]
                if suum >= target:
                    leng = j - i +1
                    min_len = min(min_len, leng)
            if min_len == float("inf"):
                return 0
        return min_len"""

        l = 0
        r = 0
        suum = 0
        n = len(nums)
        min_len = float("inf")
        while r < n:
            suum = suum + nums[r]
            while suum >= target:
                leng = r- l+ 1
                if leng < min_len:
                    min_len = leng
                suum= suum- nums[l]
                l = l +1
            r = r + 1       
        if min_len == float("inf"):           
            return 0
        return min_len







        
        

       