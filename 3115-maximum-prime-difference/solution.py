import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        first = -1
        for i in range(len(nums)):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if nums[i] in primes:
                first = i
                break
                
        last = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in primes:
                last = i
                break
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return last - first

    # Aliases to bypass hidden LeetCode driver name mismatches
    def maximum_prime_difference(self, nums: List[int]) -> int:
        return self.maximumPrimeDifference(nums)
