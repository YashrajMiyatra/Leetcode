class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.
        
        This solution utilizes Python's C-optimized string slicing `[::-1]` which 
        significantly outperforms manual mathematical division/modulo loops in Python.
        
        Time Complexity: O(log(x)) roughly equivalent to the number of digits.
        Space Complexity: O(log(x)) to store the string representation.
        """
        if x == 0:
            return 0
            
        if x < 0:
            # Slicing is executed entirely in C and avoids Python loop overhead
            res = -int(str(-x)[::-1])
            # Return 0 if outside the 32-bit signed integer range
            return res if res >= -2147483648 else 0
        else:
            res = int(str(x)[::-1])
            return res if res <= 2147483647 else 0
