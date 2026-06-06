from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            
            # Calculate current water volume
            water = (right - left) * (h_left if h_left < h_right else h_right)
            if water > max_water:
                max_water = water
                
            # Move pointer from the shorter side, skipping any elements
            # that are shorter or equal to the current height.
            if h_left < h_right:
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                while left < right and height[right] <= h_right:
                    right -= 1
                    
        return max_water
