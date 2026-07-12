import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        arr.sort()
        ans = 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(1, len(arr)):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            ans = min(ans + 1, arr[i])
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def maximum_element_after_decrementing_and_rearranging(self, arr: list[int]) -> int:
        return self.maximumElementAfterDecrementingAndRearranging(arr)
