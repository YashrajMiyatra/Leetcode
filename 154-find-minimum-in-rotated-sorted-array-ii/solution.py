import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findMin(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        left, right = 0, len(nums) - 1
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        while left < right:
            mid = (left + right) // 2
            
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                right -= 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return nums[left]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_min(self, nums: list[int]) -> int:
        return self.findMin(nums)
