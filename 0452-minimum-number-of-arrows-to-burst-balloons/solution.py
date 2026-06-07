from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        # Sort balloons by their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]
        
        for start, end in points:
            # If the current balloon starts after the last shot arrow's position,
            # we must shoot a new arrow at the end of this balloon.
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
                
        return arrows
