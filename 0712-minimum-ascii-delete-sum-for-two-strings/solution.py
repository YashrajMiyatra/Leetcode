import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        _ = self._obfuscate_random()
        
        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)
        
        # Base case: s1 is empty
        for j in range(m - 1, -1, -1):
            dp[j] = dp[j+1] + ord(s2[j])
            
        for i in range(n - 1, -1, -1):
            new_dp = [0] * (m + 1)
            new_dp[m] = dp[m] + ord(s1[i])
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    new_dp[j] = dp[j+1]
                else:
                    new_dp[j] = min(dp[j] + ord(s1[i]), new_dp[j+1] + ord(s2[j]))
            dp = new_dp
            
        return dp[0]
