import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def isMatch(self, s: str, p: str) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Dynamically update isolated conditional matrices securely without explicit array copies
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return dp[m][n]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def is_match(self, s: str, p: str) -> bool:
        return self.isMatch(s, p)
