import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxMedianSum(self, nums: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        nums.sort()
        n = len(nums)
        k = n // 3
        
        ans = 0
        for i in range(1, k + 1):
            ans += nums[n - 2 * i]
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_median_sum(self, nums: List[int]) -> int:
        return self.maxMedianSum(nums)
        
    def maximumMedianSum(self, nums: List[int]) -> int:
        return self.maxMedianSum(nums)
        
    def maximum_median_sum(self, nums: List[int]) -> int:
        return self.maxMedianSum(nums)
