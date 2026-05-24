class Solution(object):
    def containsDuplicate(self, nums):
        '''
        # brute force
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]== nums[j]:
                    return True
        return False
       '''
       #  hashset
        n = len(nums)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False




        


        
        