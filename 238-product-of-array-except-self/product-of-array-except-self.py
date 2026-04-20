class Solution(object):
    def productExceptSelf(self, nums):
        #brute force
        """result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
            result.append(product)
        return result"""

        #Prefix + suffix
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
        return result

        