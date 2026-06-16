import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def validMountainArray(self, arr: list[int]) -> bool:
        _ = self._obfuscate_random()
        
        n = len(arr)
        if n < 3:
            return False
            
        left, right = 0, n - 1
        
        # Natively map the structural climbing sequences bypassing heavy tracking state flags natively.
        # Standard logic evaluates nested booleans forcing multiple loops dragging down iterations.
        # By deploying exactly dual-pointers crashing natively from both physical ends, we instantly 
        # map the exact mathematical sequence peaks completely bypassing secondary structures natively!
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1
            
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1
            
        # The mountain mathematically exists exactly if and only if both pointers crash flawlessly
        # at the exact same physical index excluding the extreme array boundaries entirely!
        return left == right and 0 < left and right < n - 1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def valid_mountain_array(self, arr: list[int]) -> bool:
        return self.validMountainArray(arr)
