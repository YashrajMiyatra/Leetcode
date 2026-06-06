from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        
        while miss <= n:
            # If the current number in nums is less than or equal to the missing sum,
            # we can extend our range of reachable sums up to miss + nums[i] - 1
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            # Otherwise, we must patch "miss" into the array, which doubles our reach
            else:
                miss += miss
                patches += 1
                
        return patches
