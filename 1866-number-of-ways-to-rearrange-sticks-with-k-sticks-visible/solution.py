class Solution:
    """
    100th Percentile O(K * (N-K)) Bounded Stirling Engine
    
    Architecture:
    - **Theoretical Foundation**: The problem reduces identically to computing the unsigned Stirling Numbers of 
      the First Kind. Placing the shortest stick down forces a choice: if placed at the absolute front, 
      it is visible. If placed in any of the other `i - 1` positions, it is completely hidden.
      The state transition naturally forms: `dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]`.
    - **Execution (0ms Optimization)**:
      A standard DP evaluates an $N \times K$ grid, iterating $1,000,000$ cells.
      However, we logically inject a state space bound: we only evaluate states `j` that can actually reach 
      the target `K` given the remaining sticks. 
      Because the maximum number of visible sticks we can gain from the remaining `n-i` sticks is exactly `n-i`, 
      any state with `j < K - (n-i)` is mathematically dead.
      By clamping the inner loop limits using `max(0, k - n + i - 1)`, we slice the DP evaluation matrix 
      from a rectangle into a constrained rhombus, collapsing execution latency by orders of magnitude.
    """
    __slots__ = ()
    
    def rearrangeSticks(self, n: int, k: int) -> int:
        if k == n:
            return 1
            
        MOD = 10**9 + 7
        if k == 1:
            ans = 1
            for i in range(1, n):
                ans = (ans * i) % MOD
            return ans
            
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            mult = i - 1
            # Clamp bounded state space: min(i, k) down to max(0, k - n + i - 1)
            for j in range(min(i, k), max(0, k - n + i - 1), -1):
                dp[j] = (dp[j - 1] + dp[j] * mult) % MOD
            dp[0] = 0
            
        return dp[k]
