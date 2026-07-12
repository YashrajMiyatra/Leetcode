import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]
