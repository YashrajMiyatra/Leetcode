import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minPairSum(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        nums.sort()
        n = len(nums)
        max_sum = 0
        
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
            
        return max_sum
