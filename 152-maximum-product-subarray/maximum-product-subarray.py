class Solution(object):
    def maxProduct(self, nums):
        """
        n = len(nums)
        ans = nums[0]
        i = 0
        while i < n:
            product = 1
            j = i
            i = i+1
            while j<n:
                product = product * nums[j]
                ans = max(ans, product)
                j = j+1
        return ans"""

        # return max product
        # maxprod = 3 possibilities : a[i], premax * a[i] and prevmin * a[i] same for minprod = a[i], premax * a[i] and prevmin * a[i] and take max from maxprod and min from minprod and return max

        maxending = nums[0]
        minending = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            temp = maxending
            max1 = maxending * nums[i]
            max2 = minending * nums[i]
            max3 = nums[i]
            maxending = max(max1, max2, max3)
            min1 = temp * nums[i]
            min2 = minending * nums[i]
            min3 = nums[i]
            minending = min(min1, min2, min3)
            ans = max(ans, maxending)
        return ans
        
        