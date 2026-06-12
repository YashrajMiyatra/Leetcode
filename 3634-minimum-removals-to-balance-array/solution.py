import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumRemovals(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        nums.sort()
        n = len(nums)
        max_kept = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            if j - i > max_kept:
                max_kept = j - i
        return n - max_kept

    # Alias to bypass LeetCode driver mismatch
    def minRemoval(self, nums: list[int], k: int) -> int:
        return self.minimumRemovals(nums, k)
