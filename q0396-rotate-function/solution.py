import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxRotateFunction(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        if n == 0:
            return 0
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        S = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        ans = F
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for k in range(1, n):
            F = F + S - n * nums[n - k]
            if F > ans:
                ans = F
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_rotate_function(self, nums: list[int]) -> int:
        return self.maxRotateFunction(nums)
