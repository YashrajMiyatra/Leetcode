class Solution:
    """
    Constant Space Dynamic Programming Algorithm for Grid Painting.
    
    Architecture:
    - **Mathematical State Reduction**: A 1x3 row can only have two distinct color patterns:
      1. ABA (2 colors, e.g., Red-Yellow-Red). There are exactly 3*2*1 = 6 such permutations.
      2. ABC (3 colors, e.g., Red-Yellow-Green). There are exactly 3*2*1 = 6 such permutations.
    - **Transition Matrix**:
      By analyzing adjacent non-conflicting rows, we can map exact transitions:
      - An ABA row can transition to 3 valid ABA rows and 2 valid ABC rows.
      - An ABC row can transition to 2 valid ABA rows and 2 valid ABC rows.
    - **Execution**: We simply iterate from 2 to N, applying these mathematical transitions 
      while performing modulo arithmetic to prevent integer overflow and meet the prompt's 
      10^9 + 7 constraint.
    - Time Complexity: O(N) strict.
    - Space Complexity: O(1) strict.
    """
    def numOfWays(self, n: int) -> int:
        # Base case for n = 1
        aba = 6
        abc = 6
        MOD = 10**9 + 7
        
        # O(N) Transition sweeps
        for _ in range(n - 1):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD
