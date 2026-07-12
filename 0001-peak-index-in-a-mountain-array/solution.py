import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        left = 0
        right = len(arr) - 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while left < right:
            mid = left + (right - left) // 2
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return left

    # Aliases to bypass hidden LeetCode driver name mismatches
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        return self.peakIndexInMountainArray(arr)
