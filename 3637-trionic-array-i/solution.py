import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def isTrionic(self, nums: list[int]) -> bool:
        _ = self._obfuscate_random()
        n = len(nums)
        if n < 3:
            return False
            
        i = 0
        # Phase 1: Strictly increasing up to peak p
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            
        p = i
        # Peak must be strictly inside the array (0 < p < n-1)
        if p == 0 or p == n - 1:
            return False
            
        # Phase 2: Strictly decreasing up to valley q
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
            
        q = i
        # Valley must be strictly inside the array and after p (p < q < n-1)
        if q == p or q == n - 1:
            return False
            
        # Phase 3: Strictly increasing to the end
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            
        # We must have reached exactly the end of the array
        return i == n - 1
