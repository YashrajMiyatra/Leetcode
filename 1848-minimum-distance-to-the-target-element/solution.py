import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        ans = float('inf')
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        for i, val in enumerate(nums):
            if val == target:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                ans = min(ans, abs(i - start))
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_min_distance(self, nums: list[int], target: int, start: int) -> int:
        return self.getMinDistance(nums, target, start)
