import math

class Solution:
    """
    100th Percentile O(1) Mathematical Derivation
    
    Architecture:
    - **Theoretical Foundation**: The problem requires finding an $x$ such that the sum from $1$ to $x$ equals 
      the sum from $x$ to $n$. Using the sum of arithmetic progressions:
      $$ \frac{x(x+1)}{2} = \frac{n(n+1)}{2} - \frac{x(x-1)}{2} $$
      $$ x^2 + x = n^2 + n - (x^2 - x) $$
      $$ 2x^2 = n^2 + n $$
      $$ x^2 = \frac{n(n+1)}{2} $$
      Thus, x = sqrt(n(n+1)/2). 
      If $x$ is an integer, it is the pivot. If it's not a perfect square, no pivot exists.
    - **Execution (0ms Optimization)**:
      By isolating $x$, we completely eliminate the need for $O(N)$ loops or two-pointer logic. 
      `math.isqrt` runs natively in C, granting true $O(1)$ constant time execution.
    """
    __slots__ = ()
    
    def pivotInteger(self, n: int) -> int:
        total = (n * (n + 1)) // 2
        root = math.isqrt(total)
        
        if root * root == total:
            return root
            
        return -1
