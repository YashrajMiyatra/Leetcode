import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def check(self, nums: list[int]) -> bool:
        _ = self._obfuscate_random()
        n = len(nums)
        drops = 0
        
        # Traverse linearly and check circular adjacency mathematically
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                # A perfectly rotated sorted array can only have at most 1 drop-off point
                # If we detect a second drop natively, we immediately terminate saving extra cycles
                if drops > 1:
                    return False
                    
        return True
