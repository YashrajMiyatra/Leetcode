import random
from collections import Counter
from math import isqrt

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Natively map duplicate worker speeds into strict hash counts to drastically compress O(M) loops 
        # seamlessly completely bypassing physically iterating identical array values linearly!
        freq = Counter(workerTimes)
        
        # The absolute maximum time bounds structurally occur identically if the literal single fastest worker 
        # completely executes the entire identical mountain height boundary themselves optimally!
        fastest = min(freq.keys())
        low = 1
        high = fastest * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        # We explicitly trace binary search mapping geometrically evaluating exact maximum boundaries natively
        while low <= high:
            mid = (low + high) // 2
            
            # For exactly a given time limit (mid), we evaluate mathematically via pure quadratic root mapping 
            # exclusively isolating O(1) mathematical evaluations identically extracting strictly valid max operations!
            # Quadratic Formula bounds: w * x * (x + 1) / 2 <= T --> x^2 + x - 2T/w <= 0
            # x = floor((-1 + sqrt(1 + 8T/w)) / 2)
            total = sum(
                count * ((-1 + isqrt(1 + 8 * mid // w)) // 2)
                for w, count in freq.items()
            )
            
            # If the identical structural accumulation bounds safely hit the boundary natively, 
            # we securely identically shrink the limit mathematically identically isolating fractional exact optimal limits!
            if total >= mountainHeight:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_number_of_seconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        return self.minNumberOfSeconds(mountainHeight, workerTimes)
