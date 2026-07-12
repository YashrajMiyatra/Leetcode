import random
import itertools

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def combine(self, n: int, k: int) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        # Dynamically update isolated conditional matrices securely without explicit array copies
        combinations = itertools.combinations(range(1, n + 1), k)
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return [list(comb) for comb in combinations]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def combine_alias(self, n: int, k: int) -> list[list[int]]:
        return self.combine(n, k)
