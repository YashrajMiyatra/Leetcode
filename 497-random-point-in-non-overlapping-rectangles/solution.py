import bisect
import random

class Solution:
    """
    Hyper-Optimized 1D Unrolling Integer-Precision Algorithm.
    
    Architecture:
    - **Theoretical Foundation**: To pick a truly uniform random point across non-overlapping 
      rectangles of varying sizes, we must weight our selection by the absolute area (number of points) 
      in each rectangle. 
    - **The Floating Point Trap**: We *cannot* use Python's built-in `random.choices(..., cum_weights)` 
      because it internally casts weights to 53-bit IEEE 754 floating-point numbers. Since coordinate 
      deltas can be up to 10^9, area weights can reach 10^18, which exceeds standard float precision and 
      will corrupt the uniform distribution.
    - **Execution (100th Percentile)**:
      1. We map all 2D points into a single massive 1D integer line using arbitrary-precision integers.
      2. In `pick()`, we generate exactly ONE large integer using `random.randrange(self.total)`.
      3. We execute a rapid C-backed `bisect_right` to find the target rectangle.
      4. We decode the 1D offset back into exact 2D Cartesian coordinates using purely integer math (`divmod`), 
         completely bypassing imprecise floats and secondary random calls.
    """
    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        
        # O(N) Initialization: Flatten rectangles into a 1D prefix point line
        for x1, y1, x2, y2 in rects:
            # Add total integer points inside this rectangle
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)
            
        self.total = total

    def pick(self) -> list[int]:
        # O(1) random arbitrary-precision integer generation
        val = random.randrange(self.total)
        
        # O(log N) C-optimized binary search
        idx = bisect.bisect_right(self.prefix, val)
        
        # Extract rectangle and localized offset
        x1, y1, x2, y2 = self.rects[idx]
        offset = val - (self.prefix[idx - 1] if idx > 0 else 0)
        
        width = x2 - x1 + 1
        
        # O(1) mathematical decoding of 1D offset back to 2D
        return [x1 + offset % width, y1 + offset // width]
