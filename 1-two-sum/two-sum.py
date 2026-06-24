class Solution(object):
    def twoSum(self, nums, target):
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    """
        """
        hashmap = {}
        n = len(nums)
        for i in range(n):
            required = target - nums[i]
            if required in hashmap:
                return hashmap[required],i
            hashmap[nums[i]] = i
            """
        arr =[]
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            currentsum = arr[left][0] + arr[right][0]
            if currentsum == target:
                return [arr[left][1], arr[right][1]]

            elif currentsum<target:
                left = left +1
            else:
                right= right-1



        

        
        