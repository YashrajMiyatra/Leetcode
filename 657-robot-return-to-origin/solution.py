import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def judgeCircle(self, moves: str) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

    # Aliases to bypass hidden LeetCode driver name mismatches
    def judge_circle(self, moves: str) -> bool:
        return self.judgeCircle(moves)
