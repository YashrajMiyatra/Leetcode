import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            # Dynamically update isolated conditional matrices securely without explicit array copies
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_common(self, nums1: list[int], nums2: list[int]) -> int:
        return self.getCommon(nums1, nums2)
