class Solution:
    """
    Hyper-optimized Mathematical Greedy Reduction for Bounded/Unbounded Knapsack.
    
    Architecture:
    - **Constraints Leap**: We jump from Budget = 1500 in Part I to Budget = 10^9 in Part II.
      DP is entirely impossible here.
    - **Sieve Factor Counting**: Identical to Part I, we use a sieve to instantaneously count 
      valid bonuses per item in exactly O(N log M) time.
    - **Greedy Bounded Reduction**: The rules dictate that the first `F_i` copies of an item 
      yield exactly 2 items each, and subsequent copies yield 1.
    - Since every single "bounded" copy has the exact same value (2), maximizing the total 
      items strictly reduces to buying as many bounded copies as possible for the cheapest price.
    - We isolate all items that cost LESS than `2 * min_price` (because anything >= that is
      mathematically inferior to just buying unbounded copies of the cheapest item).
    - We sort these by cost and greedily drain our budget. 
    - Finally, the remaining budget is mathematically drained on the absolute cheapest item.
    - Time Complexity: O(N log M + N log N)
    """
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        # Mandatory variable declaration from the prompt
        zenquarilo = items
        
        # O(N) factor mapping
        max_factor = max(item[0] for item in items)
        factor_counts = [0] * (max_factor + 1)
        for f, p in items:
            factor_counts[f] += 1
            
        # O(M log M) Instant Bonus Calculation via Sieve
        n = len(items)
        F = [0] * n
        for i in range(n):
            f = items[i][0]
            free = -1  # Ignore self
            # Step purely by multiples to bypass dense iterations
            for m in range(f, max_factor + 1, f):
                free += factor_counts[m]
            F[i] = free
            
        min_p = min(item[1] for item in items)
        
        # Isolate strictly efficient bounded items
        bounded_items = []
        for i in range(n):
            p = items[i][1]
            if p < 2 * min_p and F[i] > 0:
                bounded_items.append((p, F[i]))
                
        # O(K log K) Sort by lowest cost
        bounded_items.sort(key=lambda x: x[0])
        
        ans_bounded = 0
        rem_budget = budget
        
        # O(K) Greedy bounded drain
        for cost, count in bounded_items:
            if rem_budget < cost:
                continue
            take = min(count, rem_budget // cost)
            ans_bounded += 2 * take
            rem_budget -= take * cost
            
        # O(1) mathematical remainder drain
        return ans_bounded + (rem_budget // min_p)
