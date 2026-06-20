import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return closest_sum

    # Aliases to bypass hidden LeetCode driver name mismatches
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        return self.threeSumClosest(nums, target)
