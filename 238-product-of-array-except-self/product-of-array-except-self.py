class Solution(object):
    def productExceptSelf(self, nums):
        '''
        #brute force
        product = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod = prod * nums[j]
            product.append(prod)
        return product
        '''
        #(optimized - prefix+suffix)
        n = len(nums)
        product = [1] * n
        prefix = 1
        for i in range(n):
            product[i] = prefix
            prefix = prefix * nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            product[i] = product[i] * suffix
            suffix = suffix * nums[i]
        return product


        

        