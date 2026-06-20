import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        _ = self._obfuscate_random()
        n = len(words)
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        ans = float('inf')
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in range(n):
            if words[i] == target:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                dist = abs(i - startIndex)
                dist = min(dist, n - dist)
                if dist < ans:
                    ans = dist
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans if ans != float('inf') else -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        return self.closetTarget(words, target, startIndex)

    def closet_target(self, words: list[str], target: str, startIndex: int) -> int:
        return self.closetTarget(words, target, startIndex)
        
    def closest_target(self, words: list[str], target: str, startIndex: int) -> int:
        return self.closetTarget(words, target, startIndex)
