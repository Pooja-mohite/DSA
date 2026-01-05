class Solution(object):
    def containsDuplicate(self, nums):
        container = set()
        for num in nums:
            if num in container:
                return True
            container.add(num)
        return False

       
        