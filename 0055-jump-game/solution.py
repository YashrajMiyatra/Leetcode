from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0
        
        for i in range(n):
            # If current index is unreachable, we can't reach the end
            if i > furthest:
                return False
                
            # Update the maximum reachable index
            if i + nums[i] > furthest:
                furthest = i + nums[i]
                
            # Early exit if we can already reach the last index
            if furthest >= n - 1:
                return True
                
        return True
