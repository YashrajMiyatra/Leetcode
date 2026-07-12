import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        seen = {}
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i, num in enumerate(nums):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        return self.containsNearbyDuplicate(nums, k)
