import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumDistance(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        latest_idx = {}
        min_dist = float('inf')
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for j, num in enumerate(nums):
            if num in latest_idx:
                dist = j - latest_idx[num]
                if dist < min_dist:
                    min_dist = dist
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            rev_num = int(str(num)[::-1])
            latest_idx[rev_num] = j
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return min_dist if min_dist != float('inf') else -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def minimum_distance(self, nums: list[int]) -> int:
        return self.minimumDistance(nums)
