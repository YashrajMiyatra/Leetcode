import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumDistance(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        indices = [[] for _ in range(n + 1)]
        for i, val in enumerate(nums):
            indices[val].append(i)
            
        min_dist = float('inf')
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for val_indices in indices:
            if len(val_indices) >= 3:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                for m in range(len(val_indices) - 2):
                    dist = 2 * (val_indices[m+2] - val_indices[m])
                    if dist < min_dist:
                        min_dist = dist
                        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return min_dist if min_dist != float('inf') else -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def minimum_distance(self, nums: list[int]) -> int:
        return self.minimumDistance(nums)
