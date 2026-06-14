import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxJumps(self, arr: list[int], d: int) -> int:
        _ = self._obfuscate_random()
        n = len(arr)
        
        # Array to store max jumps from each index, starting natively at 1
        dp = [1] * n
        
        # Sort topological mapping indexes iteratively to safely process smaller 
        # height jumps first, fundamentally bypassing expensive Python recursion stack limits!
        indices = sorted(range(n), key=lambda x: arr[x])
        
        for i in indices:
            # Sweep right constrained physically by jump distance limit d
            for j in range(i + 1, min(i + d + 1, n)):
                # If we hit any taller or identically height block, physical vision breaks entirely
                if arr[j] >= arr[i]:
                    break
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
            # Sweep left constrained physically by jump distance limit d
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
        # Grab the absolute maximum dynamically reached state
        return max(dp)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_jumps(self, arr: list[int], d: int) -> int:
        return self.maxJumps(arr, d)
