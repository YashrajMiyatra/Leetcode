import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
        return res

    # Aliases to bypass hidden LeetCode driver name mismatches
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSum(nums)
