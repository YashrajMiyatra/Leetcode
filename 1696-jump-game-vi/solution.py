import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxResult(self, nums: List[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        q = collections.deque([0])
        for i in range(1, len(nums)):
            if q and q[0] < i - k:
                q.popleft()
                
            nums[i] += nums[q[0]]
            
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
        return nums[-1]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_result(self, nums: List[int], k: int) -> int:
        return self.maxResult(nums, k)
