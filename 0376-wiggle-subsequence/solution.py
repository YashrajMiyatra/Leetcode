from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
            
        # The first element always counts towards the wiggle length
        length = 1
        prev_diff = 0
        
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if diff > 0 and prev_diff <= 0:
                length += 1
                prev_diff = diff
            elif diff < 0 and prev_diff >= 0:
                length += 1
                prev_diff = diff
                
        return length
