import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxTotalValue(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        max_val = max(nums)
        min_val = min(nums)
        return k * (max_val - min_val)

    # Alias to prevent any driver mismatches
    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        return self.maxTotalValue(nums, k)
