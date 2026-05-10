class Solution(object):
    def trap(self, height):
        """
        # brute force
        total_water = 0
        for i in range(len(height)):
            left_max = 0
            for j in range(i+1):
                left_max = max(left_max, height[j])
            
            right_max = 0
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])

            water = min(left_max, right_max) - height[i]
            total_water = total_water + water
        return total_water
        """

        #two pointers
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        total_water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water = total_water + left_max - height[left]
                left = left + 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water = total_water + right_max- height[right]
                right = right - 1
        return total_water

        
        