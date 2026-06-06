from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        furthest = 0
        
        for i in range(n - 1):
            # Update the furthest index reachable from current steps
            if i + nums[i] > furthest:
                furthest = i + nums[i]
                
            # If we reached the end of the current jump coverage,
            # we must take another jump and update the range.
            if i == current_end:
                jumps += 1
                current_end = furthest
                # Early exit if we can already reach the final index
                if current_end >= n - 1:
                    break
                    
        return jumps
