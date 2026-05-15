class Solution(object):
    def maxArea(self, height):
        """
        water = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                h = min(height[i], height[j])
                width = j - i
                area = h * width
                water = max(water, area)
        return water
        """
        water = 0
        left = 0
        right = len(height) - 1
        while left<right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width
            water = max(area, water)
            if height[left] < height[right]:
                left = left + 1
            else:
                right= right - 1
        return water

            
       

        