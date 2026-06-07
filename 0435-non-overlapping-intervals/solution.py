from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        removed = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            # If the current interval starts after or at the end of the previous one,
            # we keep it and update the end boundary.
            if start >= prev_end:
                prev_end = end
            else:
                # Otherwise, it overlaps, so we must remove it.
                removed += 1
                
        return removed
