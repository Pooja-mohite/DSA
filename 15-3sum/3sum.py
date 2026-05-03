class Solution(object):
        def threeSum(self, nums):
            '''
            #Brute force
            n = len(nums)
            tsum = set()
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        if nums[i]+nums[j]+nums[k] == 0:
                            result = tuple(sorted([nums[i],nums[j],nums[k]]))
                            tsum.add(result)
            return list(tsum)
            '''
            #optimized(two pointers)
            n= len(nums)
            nums.sort()
            tsum = []
            
            for i in range(n):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                left = i+1
                right = n-1
                while left < right:
                    if nums[i]+nums[left]+nums[right] ==0:
                        tsum.append([nums[i],nums[left],nums[right]])
                        left = left +1
                        right = right - 1
                        while left<right and nums[left] == nums[left-1]:
                            left = left + 1
                        while left< right and nums[right] == nums[right+1]:
                            right = right-1
                    elif nums[i]+nums[left]+nums[right] < 0:
                        left = left +1
                    else:
                        right = right-1
            return tsum

            