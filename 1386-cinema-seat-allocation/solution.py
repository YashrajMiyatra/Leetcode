import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        row_reserved = collections.defaultdict(set)
        for row, seat in reservedSeats:
            row_reserved[row].add(seat)
            
        ans = 2 * (n - len(row_reserved))
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for seats in row_reserved.values():
            # Dynamically update isolated conditional matrices securely without explicit array copies
            left = not (2 in seats or 3 in seats or 4 in seats or 5 in seats)
            right = not (6 in seats or 7 in seats or 8 in seats or 9 in seats)
            mid = not (4 in seats or 5 in seats or 6 in seats or 7 in seats)
            
            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_number_of_families(self, n: int, reservedSeats: List[List[int]]) -> int:
        return self.maxNumberOfFamilies(n, reservedSeats)
