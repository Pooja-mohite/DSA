class Solution(object):
    def findDuplicate(self, nums):
        n =len(nums)
        hashset = set()
        for i in range(n):
            if nums[i] in hashset:
                return nums[i]
            hashset.add(nums[i])
       
       