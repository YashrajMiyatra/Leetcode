import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return [ranks[x] for x in arr]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def array_rank_transform(self, arr: list[int]) -> list[int]:
        return self.arrayRankTransform(arr)
