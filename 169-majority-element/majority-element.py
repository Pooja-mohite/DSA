class Solution(object):
    def majorityElement(self, nums):
        '''
        #brute force
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count = count + 1
            if count > n // 2:
                return nums[i]
                '''
        count = 0
        number = 0
        for num in nums:
            if count == 0:
                number = num
            if num == number:
                count = count + 1
            else:
                count = count - 1
        return number
        
        

       
        