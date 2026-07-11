class Solution(object):
    def removeDuplicates(self, nums):
        
        temparray = []
        for num in nums:
            if num not in temparray:
                temparray.append(num)
        for i in range(len(temparray)):
            nums[i] = temparray[i]
        return len(temparray)

        """
        n = len(nums)
        for i in range(n):
            unique = 1
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    continue
                else:
                    nums[i+1] = nums[j]
               
            unique = unique+1
        return unique
        """
       