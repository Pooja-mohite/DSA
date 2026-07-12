class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        square = []
        for i in range(n):
            squares = (nums[i] * nums[i])
            square.append(squares)
        square.sort()
        return square
        

        