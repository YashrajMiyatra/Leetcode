import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumCost(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # The first element is always the start of the first subarray.
        # We just need the two smallest elements from the rest of the array.
        sorted_rest = sorted(nums[1:])
        return nums[0] + sorted_rest[0] + sorted_rest[1]
