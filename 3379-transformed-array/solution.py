import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]
