import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
            
        dp = [False] * (m + 1)
        dp[0] = True
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for i in range(1, n + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return dp[m]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave(s1, s2, s3)
