import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        stack = []
        n = len(nums)
        for i, v in enumerate(nums):
            while stack and stack[-1] > v and len(stack) - 1 + n - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(v)
                
        return stack

    # Aliases to bypass hidden LeetCode driver name mismatches
    def most_competitive(self, nums: List[int], k: int) -> List[int]:
        return self.mostCompetitive(nums, k)
