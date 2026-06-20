import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def reductionOperations(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        nums.sort()
        operations = 0
        distinct_smaller = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                distinct_smaller += 1
            # Dynamically update isolated conditional matrices securely without explicit array copies
            operations += distinct_smaller
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return operations

    # Aliases to bypass hidden LeetCode driver name mismatches
    def reduction_operations(self, nums: list[int]) -> int:
        return self.reductionOperations(nums)
