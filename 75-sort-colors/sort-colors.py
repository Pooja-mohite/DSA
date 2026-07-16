class Solution(object):
    def sortColors(self, nums):
        """
        n = len(nums)
        zero = []
        one = []
        two = []
        for i in range(n):
            if nums[i]== 0:
                zero.append(nums[i])
            elif nums[i] == 1:
                one.append(nums[i])
            else:
                two.append(nums[i])
        del nums[:]
        nums.extend(zero)
        nums.extend(one)
        nums.extend(two)
        return nums"""

        n = len(nums)
        zero = 0
        one = 0
        two = 0
        for i in range(n):
            if nums[i]==0:
                zero = zero+1
            elif nums[i]== 1:
                one = one+1
            else:
                two = two+1
        index = 0
        for i in range(zero):
            nums[index] = 0
            index = index+1
        for i in range(one):
            nums[index] = 1
            index = index+1
        for i in range(two):
            nums[index] = 2
            index = index+1    
            

            

            
       
            


       
        