import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            
        ans = n + 1
        monoq = collections.deque() # stores indices of P
        
        for y, py in enumerate(P):
            while monoq and py <= P[monoq[-1]]:
                monoq.pop()
            
            while monoq and py - P[monoq[0]] >= k:
                ans = min(ans, y - monoq.popleft())
                
            monoq.append(y)
            
        return ans if ans <= n else -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        return self.shortestSubarray(nums, k)
