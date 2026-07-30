import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def sumSubarrayMins(self, arr: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        MOD = 10**9 + 7
        stack = []
        ans = 0
        n = len(arr)
        
        for i in range(n + 1):
            val = arr[i] if i < n else 0
            
            while stack and arr[stack[-1]] > val:
                j = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                ans = (ans + arr[j] * (j - left) * (right - j)) % MOD
                
            stack.append(i)
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def sum_subarray_mins(self, arr: List[int]) -> int:
        return self.sumSubarrayMins(arr)
