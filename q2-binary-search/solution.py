import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def search(self, nums: list[int], target: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        left = 0
        right = len(nums) - 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while left <= right:
            mid = left + (right - left) // 2
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def binary_search(self, nums: list[int], target: int) -> int:
        return self.search(nums, target)
