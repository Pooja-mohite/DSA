class Solution(object):
        def threeSum(self, nums):
            # BRUTE fORCE
            """
            n = len(nums)
            tsum = []
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        if nums[i]+ nums[j]+nums[k] == 0:
                            summ = sorted([nums[i],nums[j],nums[k]])
                            if summ not in tsum:
                                tsum.append(summ)
            return tsum 
            """
            """n= len(nums)
            tsum = set()
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        if nums[i]+nums[j]+nums[k] == 0:
                            summ = tuple(sorted([nums[i], nums[j], nums[k]]))
                            tsum.add(summ)
            return list(tsum)"""

            # hashset
            """result = set()
            n = len(nums)
            for i in range(n):
                hashmap = set()
                for j in range(i+1,n):
                    target = -(nums[i]+nums[j])
                    if target in hashmap:
                        tsum = [nums[i],nums[j], target]
                        tsum.sort()
                        result.add(tuple(tsum))    
                    else:
                        hashmap.add(nums[j])
            return list(result)"""

            #Two poinrtr
            nums.sort()
            result = []
            n =len(nums)
            for i in range(n):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                left = i+1
                right = n-1
                while left<right:
                    if nums[i]+nums[left]+nums     [right] == 0:
                        result.append([nums[i],nums[left],nums[right]])
                        left = left+1
                        right= right-1
                        while left<n and nums      [left] == nums[left-1]:
                            left = left+1
                        while right>= 0 and nums[right]==nums[right+1]:
                            right = right -1
                    elif nums[i]+nums[left]+nums[right] < 0:
                        left = left+1
                    else:
                        right= right-1
            return result






            
            
            
           
           
