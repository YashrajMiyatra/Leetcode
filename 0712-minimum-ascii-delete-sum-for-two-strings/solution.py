class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Optimize space by making s2 the shorter string
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        m, n = len(s1), len(s2)
        # dp[j] stores the min ASCII delete sum for s1[:i] and s2[:j]
        dp = [0] * (n + 1)
        
        # Base case: s1 is empty, delete all characters of s2[:j]
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
            
        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] += ord(s1[i - 1])
            
            for j in range(1, n + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    # Characters match, no deletion cost added
                    dp[j] = prev_diag
                else:
                    # Choose the minimum cost between deleting s1[i-1] or s2[j-1]
                    dp[j] = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
                prev_diag = temp
                
        return dp[n]
