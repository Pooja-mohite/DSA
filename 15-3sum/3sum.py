class Solution(object):
        def threeSum(self, nums):
            #brute force
            """n = len(nums)
            result = set()
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        if nums[i] + nums[j] + nums[k] == 0:
                            temp = tuple(sorted([nums[i],nums[j],nums[k]]))
                            result.add(temp)
            return list(result)"""

            #two pointers
            nums.sort()
            n = len(nums)
            result = []
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                start = i+1
                end = n-1
                while start<end:
                    if nums[i] + nums[start] + nums[end] == 0:
                        result.append([nums[i], nums[start], nums[end]])
                        start = start + 1
                        end = end - 1
                        while start<end and nums[start] == nums[start-1]:
                            start = start + 1
                        while start<end and nums[end] == nums[end+1]:
                            end = end - 1
                    elif nums[i]+nums[start]+nums[end] < 0:
                        start = start + 1
                    else:
                        end = end - 1
            return result



           