import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        _ = self._obfuscate_random()
        
        # We can quickly segregate the array using list comprehensions in Python
        # which are highly optimized in C under the hood.
        left = [n for n in nums if n < pivot]
        middle = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]
        
        return left + middle + right
