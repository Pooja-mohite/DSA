class Solution(object):
    def maxArea(self, height):
        #brute force
        """n = len(height)
        max_water = 0
        for i in range(n):
            for j in range(i+1, n):
                h = min(height[i], height[j])
                width = j - i
                area = h * width
                max_water = max(max_water, area)
        return max_water"""

        # two pointers
        start = 0
        end = len(height)-1
        max_water = 0
        while start<end:
            h = min(height[start], height[end])
            width = end - start
            area = h * width
            max_water = max(max_water, area)
            if height[start] < height[end]:
                start = start + 1
            else:
                end = end - 1
        return max_water 

        