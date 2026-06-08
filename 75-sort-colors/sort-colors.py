class Solution(object):
    def sortColors(self, nums):
        """
        # if condition is not given
        nums.sort()
        """
        #  brute force
        """
        n= len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    """
        # two pointers  
        '''           
        n = len(nums)            
        left = 0
        right = n-1
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left = left + 1
        for i in range(n-1,-1,-1):
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right = right - 1
                '''
        # 3 pointers(dutch national flag)
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while mid<= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low = low + 1
                mid = mid+1
            elif nums[mid] == 1:
                mid = mid+1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1
            


       
        