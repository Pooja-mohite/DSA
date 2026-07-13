import math
class Solution(object):
    def sortedSquares(self, nums):
        #brute force
        """
        n = len(nums)
        square = []
        for i in range(n):
            squares = (nums[i] * nums[i])
            square.append(squares)
        square.sort()
        return square"""

        #two pointer

        """n = len(nums)
        left = 0
        right = n - 1
        ans = [0] * n
        index = n - 1

        while left <= right:

            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare > rightSquare:
                ans[index] = leftSquare
                left = left + 1
            else:
                ans[index] = rightSquare
                right = right - 1

            index = index - 1
        return ans"""

        """n = len(nums)
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        #no negative numbers
        if len(neg) == 0:
            return [x * x for x in pos]
        
        # n o positive numbers
        if len(pos) ==0:
            square = [x *x for x in neg]
            square.reverse()
            return square
        
        # both neg and pos exists
        neg = [x *x for x in neg]
        neg.reverse()
        pos = [x *x for x in pos]
        p = len(neg)
        q = len(pos)
        square = []
        i = 0
        j = 0
        while i<p and j<q:
            if neg[i] <= pos[j]:
                square.append(neg[i])
                i = i+1
            else:
                square.append(pos[j])
                j = j+1
        while  i< p:
                square.append(neg[i])
                i = i+1
        while j<q:
                square.append(pos[j])
                j = j+1
        return square"""
            
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] * nums[i]
        gap = (n//2) + (n%2)
        while gap > 0:
            i = 0
            j = gap
            while j < n:
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                i = i+1
                j = j+1
        
            if gap == 1:
                gap = 0
            else:
                gap = (gap//2) + (gap%2)
        return nums

             
            
            
        

        
                



        

        