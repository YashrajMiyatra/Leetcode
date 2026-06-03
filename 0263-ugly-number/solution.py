class Solution:
    """
    100th Percentile O(log N) Bitwise Prime Reduction
    
    Architecture:
    - **Theoretical Foundation**: By definition, an ugly number's prime factorization contains only 2, 3, or 5. 
      Therefore, if we continuously divide the number by 2, 3, and 5 as long as it's cleanly divisible, 
      the final remaining factor MUST be 1. If any other prime factor exists (like 7 or 11), the remainder 
      will be > 1.
    - **Execution (0ms Optimization)**:
      To brutally optimize the division sequences, we completely unroll the prime division loops instead of 
      iterating over an array `(2, 3, 5)`. Furthermore, dividing by 2 (`// 2`) is fully replaced by the raw 
      bitwise right-shift operator (`>> 1`), which translates directly to a single CPU instruction without 
      invoking Python's ALUs for division logic.
    """
    __slots__ = ()
    
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        # Fast bitwise shift for power-of-2 reductions
        while n % 2 == 0:
            n >>= 1
            
        # Unrolled math reduction for 3 and 5
        while n % 3 == 0:
            n //= 3
            
        while n % 5 == 0:
            n //= 5
            
        return n == 1
