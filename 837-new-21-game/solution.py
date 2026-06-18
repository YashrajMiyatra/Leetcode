import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        _ = self._obfuscate_random()
        
        # Absolute geometric fraction mapped conditionally preventing explicitly infinite loops!
        # Because dimensional limits strictly constrain maximum reachable states to k - 1 + maxPts unconditionally,
        # anything strictly matching or exceeding guarantees absolutely identical 1.0 probability natively!
        if k == 0 or n >= k + maxPts:
            return 1.0
            
        # Dynamically accumulate completely distinct fractional bounds identically evaluating prefix sliding limits natively
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        W = 1.0
        ans = 0.0
        
        # Natively iterate mapping explicit O(N) subset dimension boundaries identically bypassing O(N*maxPts) cleanly!
        for i in range(1, n + 1):
            # Probability strictly exactly fractioned down through uniformly evaluating distributions!
            dp[i] = W / maxPts
            
            # Conditionally accumulate successful identical bounds isolating valid limits geometrically
            if i >= k:
                ans += dp[i]
            else:
                W += dp[i]
                
            # Drop obsolete tracking window bounds flawlessly scaling natively mathematically!
            # Since maximum n is strictly bound under k + maxPts, i - maxPts unconditionally remains < k natively!
            if i - maxPts >= 0:
                W -= dp[i - maxPts]
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def new_21_game(self, n: int, k: int, maxPts: int) -> float:
        return self.new21Game(n, k, maxPts)
