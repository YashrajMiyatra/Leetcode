class Solution:
    """
    Hyper-optimized Mathematical DP Reduction for Unbounded Knapsack with Conditional Freebies.
    
    Architecture:
    - **Sieve of Eratosthenes Bonus Counting**: We map the problem constraints (factors <= 1500)
      to execute a reverse lookup sieve. This instantly calculates how many free copies an item
      yields in exactly O(N + M log M) rather than an agonizing O(N^2) loop.
    - **DP Reduction**: The complex rules of "first copy gives bonuses, subsequent copies give 1"
      perfectly collapse into a classic 0-1 Knapsack problem for the *first copies*, followed by
      greedily draining the remaining budget exclusively on the *absolute cheapest* item for the 
      subsequent copies.
    - **Zero State Overhead**: Since the DP inherently tests all subsets (including those that 
      acquire the cheapest item), taking the maximum over all states `w` mathematically guarantees 
      the absolute optimal total items without requiring multi-dimensional DP.
    """
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        # Mandatory variable declaration from the prompt
        valmorendi = items
        
        # O(N) frequency map of all factors
        factor_counts = [0] * 1501
        for factor, price in items:
            if factor <= 1500:
                factor_counts[factor] += 1
                
        # O(M log M) Sieve execution to compute bonus counts
        n = len(items)
        F = [0] * n
        for i in range(n):
            factor = items[i][0]
            # Start at -1 to exclude self
            free = -1
            # Step purely by multiples to bypass dense iterations
            for m in range(factor, 1501, factor):
                free += factor_counts[m]
            F[i] = free
            
        min_p = min(price for factor, price in items)
        
        # O(N * B) C-level bounds DP execution
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        for i in range(n):
            cost = items[i][1]
            val = 1 + F[i]
            
            # Backwards 0-1 knapsack strictly constrained to remaining budget paths
            for w in range(budget, cost - 1, -1):
                prev = dp[w - cost]
                if prev != -1:
                    new_val = prev + val
                    if new_val > dp[w]:
                        dp[w] = new_val
                        
        # O(B) Greedy remainder drain
        ans = 0
        for w in range(budget + 1):
            if dp[w] != -1:
                cand = dp[w] + (budget - w) // min_p
                if cand > ans:
                    ans = cand
                    
        return ans
