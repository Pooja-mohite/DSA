class Solution(object):
    def twoSum(self, nums, target):
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    """
        '''
        hashmap = {}
        n = len(nums)
        for i in range(n):
            required = target - nums[i]
            if required in hashmap:
                return hashmap[required],i
            hashmap[nums[i]] = i
         
    
        '''
        '''
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
                '''
        
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr.sort()
        for i in range(len(nums)):
            required = target - arr[i][0]
            left = i+1
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid][0] == required:
                    return [arr[i][1], arr[mid][1]]
                elif arr[mid][0] < required:
                    left = mid + 1
                else:
                    right = mid-1



        

        
        