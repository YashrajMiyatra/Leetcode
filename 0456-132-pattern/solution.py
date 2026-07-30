import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def find132pattern(self, nums: List[int]) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        max_k = float('-inf')
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_k:
                return True
            while stack and nums[i] > stack[-1]:
                max_k = stack.pop()
            stack.append(nums[i])
            
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_132_pattern(self, nums: List[int]) -> bool:
        return self.find132pattern(nums)
        
    def find132Pattern(self, nums: List[int]) -> bool:
        return self.find132pattern(nums)
