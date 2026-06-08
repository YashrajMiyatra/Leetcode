import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
                continue
                
            # Find the position of the first '0' from the right
            # n = ...0111...1
            # We want to flip the leftmost '1' in this contiguous block of 1s
            temp = n
            pos = 0
            while temp % 2 == 1:
                pos += 1
                temp //= 2
                
            # The bit to flip is at position (pos - 1)
            # We subtract 2**(pos - 1)
            ans.append(n - (1 << (pos - 1)))
            
        return ans
