class Solution(object):
    def sortColors(self, nums):
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
        return nums
            
       
            


       
        