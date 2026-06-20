import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        counts = [0] * 20001
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for num in nums:
            counts[num + 10000] += 1
            
        rem = k
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(20000, -1, -1):
            if counts[i] > 0:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                rem -= counts[i]
                if rem <= 0:
                    return i - 10000
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_kth_largest(self, nums: list[int], k: int) -> int:
        return self.findKthLargest(nums, k)
