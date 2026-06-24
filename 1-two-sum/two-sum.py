class Solution(object):
    def twoSum(self, nums, target):
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    """

        hashmap = {}
        n = len(nums)
        for i in range(n):
            required = target - nums[i]
            if required in hashmap:
                return hashmap[required],i
            hashmap[nums[i]] = i


        

        
        