class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer.
        
        Optimized for maximum speed by leveraging C-level string operations:
        - `lstrip()` for stripping whitespace instantly.
        - `isdigit()` over character comparison, as it operates at C speed.
        - String slicing and a single `int()` cast instead of iterative math.
        
        Time Complexity: O(n)
        Space Complexity: O(n) for the stripped string and digit slice.
        """
        s = s.lstrip()
        if not s:
            return 0
            
        n = len(s)
        i = 0
        
        # Check sign
        if s[0] == '-' or s[0] == '+':
            i = 1
            
        start = i
        
        # Fast-forward to the end of the digit sequence
        while i < n and s[i].isdigit():
            i += 1
            
        # No valid digits read
        if start == i:
            return 0
            
        # Slice the string and let Python's C-backend handle the string-to-int conversion
        res = int(s[:i])
        
        # Clamp to 32-bit signed integer boundaries
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
            
        return res
