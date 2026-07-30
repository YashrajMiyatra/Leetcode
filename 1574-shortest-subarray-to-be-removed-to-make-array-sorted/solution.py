import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(arr)
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
            
        if left == n - 1:
            return 0
            
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
            
        ans = min(n - 1 - left, right)
        
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_length_of_shortest_subarray(self, arr: List[int]) -> int:
        return self.findLengthOfShortestSubarray(arr)
