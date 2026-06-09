import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Since we can choose the same subarray multiple times, we just want to 
        # find the maximum possible value of a single subarray and multiply it by k.
        # The maximum possible value is simply the global maximum of nums minus 
        # the global minimum of nums. The entire array nums itself achieves this value.
        max_val = max(nums)
        min_val = min(nums)
        
        return k * (max_val - min_val)
