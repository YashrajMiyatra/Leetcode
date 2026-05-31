class Solution:
    """
    Bit Manipulation approach for Base 10 Complement.
    
    Architecture:
    - **Concept**: Finding the complement of a binary number is equivalent to performing an XOR 
      operation (`^`) with a bitmask of `1`s of the exact same length.
      For example, 5 is `101`. The mask of length 3 is `111` (which is 7). `5 ^ 7 = 2` (`010`).
    - **Edge Case**: `n = 0` has a bit length of 0 in Python, but its binary string is `"0"`, 
      so its complement must be `1`. We handle this with a hardcoded early return.
    - **Optimization**: We leverage Python's lightning-fast native `bit_length()` built-in 
      method to instantly generate the mask `(1 << n.bit_length()) - 1`.
    - Time Complexity: O(1).
    - Space Complexity: O(1).
    """
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        # Create a mask of 1s of the exact same length as the binary representation of n
        mask = (1 << n.bit_length()) - 1
        
        # XOR n with the mask to flip all bits
        return n ^ mask
