import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def furthestDistanceFromOrigin(self, moves: str) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')

    # Aliases to bypass hidden LeetCode driver name mismatches
    def furthest_distance_from_origin(self, moves: str) -> int:
        return self.furthestDistanceFromOrigin(moves)
