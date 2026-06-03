class Solution:
    """
    Zero-String Math-Only Architecture for Palindrome Validation
    
    Architecture:
    - **Theoretical Foundation**: The follow-up strictly prohibits casting the integer to a string. While `str(x) == str(x)[::-1]` is highly optimized in Python's C-backend, a pure mathematical reversal avoids heap-allocated string objects entirely.
    - **Execution (Extreme Optimization)**:
      1. **Early Terminations**: Negative numbers are instantly `False`. Numbers perfectly divisible by 10 (except 0) are also `False` because a palindrome cannot start with 0.
      2. **Half-Reversal**: We only reverse the SECOND HALF of the integer. Reversing the full integer could technically overflow a 32-bit signed integer (though Python handles arbitrarily large ints, this honors the physical C constraints implied by LeetCode).
      3. **Termination Condition**: The loop terminates the exact microsecond `rev` becomes >= x, meaning we've reached the exact midpoint.
      4. **Parity Agnostic**: If length is even, `x == rev`. If length is odd, the middle digit drops to `rev` but we safely ignore it via `rev // 10`.
    """
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers or multiples of 10 (excluding 0) can never be palindromes
        if x < 0 or (x and x % 10 == 0):
            return False
            
        rev = 0
        
        # Halt at exactly the midpoint to avoid reversing the entire number
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
            
        # Even length -> x == rev
        # Odd length -> x == rev // 10 (the middle digit doesn't matter)
        return x == rev or x == rev // 10
