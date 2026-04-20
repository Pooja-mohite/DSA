class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        """n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]"""

        # hashmap
        n = len(nums)
        Hashmap = {}
        for i in range(n):
            required_no = target - nums[i]
            if required_no in Hashmap:
                return [Hashmap[required_no], i]
            Hashmap[nums[i]] = i

    # two pointers(sorted array)
        
        """start = 0
        end = len(nums) - 1
        while start <= end:
            sum = nums[start] + nums[end]
            if sum == target:
                return [start, end]
            elif sum < target:
                start = start + 1
            else:
                end = end - 1"""
        


       

     
        