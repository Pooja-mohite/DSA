class Solution(object):
    def canJump(self, nums):
        #Brute Force=
        """
        n = len(nums)
        def canreach(i):
            if i >= n-1:
                return True
            max_jump = nums[i]

            for step in range(1, max_jump + 1):
                if canreach(i + step):
                    return True
            return False
        return canreach(0)
        """
        #Greedy;

        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n-1:
                return True
        return True
        