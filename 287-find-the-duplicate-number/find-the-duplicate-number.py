class Solution(object):
    def findDuplicate(self, nums):
        """
        n =len(nums)
        hashset = set()
        for i in range(n):
            if nums[i] in hashset:
                return nums[i]
            hashset.add(nums[i])"""


        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
   
        return slow
       
       