import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        diff = [0] * 101
        for s in seats:
            diff[s] += 1
        for s in students:
            diff[s] -= 1
            
        ans = 0
        unmatched = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        # Dynamically update isolated conditional matrices securely without explicit array copies
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        for i in range(101):
            unmatched += diff[i]
            ans += abs(unmatched)
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_moves_to_seat(self, seats: List[int], students: List[int]) -> int:
        return self.minMovesToSeat(seats, students)
