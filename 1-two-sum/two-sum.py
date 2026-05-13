class Solution(object):
    def twoSum(self, nums, target):
        '''
        # brute force
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    '''
        #hashmap
        hashmap = {}
        for i in range(len(nums)):
            required = target-nums[i]
            if required in hashmap:
                return [hashmap[required], i]
            hashmap[nums[i]] = i

        
        