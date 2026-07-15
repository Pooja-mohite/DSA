class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        #brute force
        n = len(nums)
        min_diff = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    tsum = nums[i]+nums[j]+nums[k]
                    diff = abs(target - tsum)
                    if min_diff > diff:
                        min_diff = diff
            
                        result = tsum
        return result"""

        """
        #  hashset
        n = len(nums)
        min_diff = float("inf")
        result = 0
        for i in range(n):
            hashmap = set()
            for j in range(i+1,n):
                num3 = target - nums[i] - nums[j]
                diff = abs(target - num3)
                if min_diff > diff:
                    min_diff = diff
                    if num3 in hashmap:
                        result = result + num3
                    else:
                        hashmap.add(num3)
        return result
        """
        # two pointer
        nums.sort()
        n = len(nums)
        min_diff = float("inf")
        result = 0
        for i in range(n-2):
            left = i+1
            right = n -1
            while left<right:
                tsum = nums[i]+nums[left]+nums[right]
                diff = abs(target - tsum)
                if min_diff > diff:
                    min_diff = diff
                    result = tsum
                if tsum == target:
                    return tsum
                if tsum < target:
                    left = left+1
                else:
                    right= right-1
        return result
                
                


    

        




       
        