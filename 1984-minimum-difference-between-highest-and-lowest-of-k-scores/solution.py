import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumDifference(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        if k == 1:
            return 0
            
        nums.sort()
        min_diff = float('inf')
        
        # Check every sliding window of size k
        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
            
        return min_diff
