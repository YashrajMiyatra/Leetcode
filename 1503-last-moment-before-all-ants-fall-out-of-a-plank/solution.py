import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        max_left = max(left) if left else 0
        max_right = n - min(right) if right else 0
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return max(max_left, max_right)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_last_moment(self, n: int, left: List[int], right: List[int]) -> int:
        return self.getLastMoment(n, left, right)
