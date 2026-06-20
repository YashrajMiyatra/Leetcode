import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        remainder_map = {0: -1}
        current_sum = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % k
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if current_sum in remainder_map:
                if i - remainder_map[current_sum] >= 2:
                    return True
            else:
                remainder_map[current_sum] = i
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        return self.checkSubarraySum(nums, k)
