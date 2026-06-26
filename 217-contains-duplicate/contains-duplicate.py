class Solution(object):
    def containsDuplicate(self, nums):
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        '''
        # sorting
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        '''
        #hashset
        hashset = set()
        for element in nums:
            if element in hashset:
                return True
            hashset.add(element)
        return False
        

        