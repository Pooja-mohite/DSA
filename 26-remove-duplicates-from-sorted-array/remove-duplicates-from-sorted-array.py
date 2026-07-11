class Solution(object):
    def removeDuplicates(self, nums):
        """
        temparray = []
        for num in nums:
            if num not in temparray:
                temparray.append(num)
        for i in range(len(temparray)):
            nums[i] = temparray[i]
        return len(temparray)
        """

        
        """n = len(nums)
        i = 0
        for j in range(1,n):
            if nums[i] == nums[j]:
                continue"""

        i = 0
        unique = 1
        for j in range(1,len(nums)):
            if nums[i] == nums[j]:
                continue
                j = j+1
            else:
                nums[i+1] = nums[j]
                j = j+1
                i = i+1
                unique = unique+1
        return unique

            
       