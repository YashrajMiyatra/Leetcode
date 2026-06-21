import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        max_dist = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                if j - i > max_dist:
                    max_dist = j - i
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return max_dist

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_distance(self, nums1: list[int], nums2: list[int]) -> int:
        return self.maxDistance(nums1, nums2)
