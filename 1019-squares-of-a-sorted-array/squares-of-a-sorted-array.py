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

        n = len(nums)
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
        return ans

        """n = len(nums)
        left = 0
        right = n-1
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
            return square"""
                



        

        