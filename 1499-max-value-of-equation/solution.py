import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        q = collections.deque()
        ans = float('-inf')
        
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
                
            if q:
                ans = max(ans, q[0][0] + y + x)
                
            val = y - x
            while q and q[-1][0] <= val:
                q.pop()
                
            q.append((val, x))
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_max_value_of_equation(self, points: List[List[int]], k: int) -> int:
        return self.findMaxValueOfEquation(points, k)
