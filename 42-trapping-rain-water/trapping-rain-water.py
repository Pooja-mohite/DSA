class Solution(object):
    def trap(self, height):
        #brute force
        '''
        totalwater = 0
        n = len(height)
        for i in range(n):
            leftmax = 0
            for j in range(i+1):
                leftmax = max(leftmax, height[j])
            rightmax = 0
            for j in range(i, n):
                rightmax = max(rightmax, height[j])
            water = min(leftmax, rightmax)- height[i]
            totalwater = totalwater + water
        return totalwater
        '''
        # using two pointers
        left = 0
        right = len(height)-1
        leftmax =0
        rightmax = 0
        totalwater = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    totalwater = totalwater + leftmax - height[left]
                left = left + 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    totalwater = totalwater + rightmax - height[right]
                right =right-1
        return totalwater 







       