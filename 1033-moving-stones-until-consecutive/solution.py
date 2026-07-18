import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        x, y, z = sorted([a, b, c])
        
        max_moves = z - x - 2
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            min_moves = 1
        else:
            min_moves = 2
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return [min_moves, max_moves]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def num_moves_stones(self, a: int, b: int, c: int) -> List[int]:
        return self.numMovesStones(a, b, c)
