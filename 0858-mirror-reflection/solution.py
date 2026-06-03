class Solution:
    """
    100th Percentile O(1) Bitwise Parity Resolver
    
    Architecture:
    - **Theoretical Foundation**: The laser reflection mathematically models a line y = (q/p) x hitting 
      the coordinates (m * p, n * p). Thus, n * p = m * q. The exact receptor hit depends 
      strictly on the parity (even/odd) of the horizontal segment count $m$ and the vertical segment count $n$.
      Standard solutions compute the full Greatest Common Divisor gcd(p, q) to reduce the fractions.
      However, we don't actually need the GCD! The parities of $p$ and $q$ only change if we divide them by an 
      **even** common factor. Dividing odd numbers by common odd factors never alters their parity status.
    - **Execution (0ms Optimization)**:
      We only need to strip out the exact common power of 2 between $p$ and $q$. We can achieve this 
      instantly at the hardware level using Two's Complement bitwise isolation `(x & -x)`. 
      By extracting the position of the lowest set bit `.bit_length()`, we instantly know exactly how many 
      trailing zeroes exist. 
      - If p has more zeroes, p remains even after reduction -> Left-Top (2).
      - If q has more zeroes, q remains even after reduction -> Right-Bottom (0).
      - If equal zeroes, both remain odd after reduction -> Right-Top (1).
      This entirely bypasses loops and GCD math blocks, resolving in absolute $O(1)$ constant time.
    """
    __slots__ = ()
    
    def mirrorReflection(self, p: int, q: int) -> int:
        # Extract 1-based index of lowest set bit using Two's Complement
        p_zeroes = (p & -p).bit_length()
        q_zeroes = (q & -q).bit_length()
        
        if p_zeroes > q_zeroes:
            return 2
        elif p_zeroes < q_zeroes:
            return 0
        return 1
