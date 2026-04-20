class Solution(object):
    def containsDuplicate(self, nums):
        #brute force
        """n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
            return False"""

        # hahset
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        


        
        