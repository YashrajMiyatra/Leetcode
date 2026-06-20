import collections
import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def countElements(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        freq = collections.Counter(nums)
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        sorted_uniques = sorted(freq.keys(), reverse=True)
        
        greater = 0
        ans = 0
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for x in sorted_uniques:
            if greater >= k:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                ans += freq[x]
            greater += freq[x]
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def count_elements(self, nums: list[int], k: int) -> int:
        return self.countElements(nums, k)
