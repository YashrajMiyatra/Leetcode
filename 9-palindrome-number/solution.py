class Solution:
    """
    Mathematical Reversal Algorithm for Palindrome Number.
    
    Architecture:
    - **Constraints**: The follow-up explicitly forbids converting the integer to a string.
    - **Optimization**: Instead of reversing the entire integer (which could theoretically cause overflow 
      in typed languages, though not an issue in Python, it's good practice), we only reverse the SECOND HALF 
      of the integer.
    - **Execution**: We continuously pop the last digit of `x` and push it onto `reverted_half` until `x` is 
      less than or equal to `reverted_half`.
    - If the number has an even length, `x` will perfectly equal `reverted_half`.
    - If the number has an odd length, `reverted_half` will have one extra digit. We discard it with `// 10` and compare.
    - Time Complexity: O(log10(x)) strict. Space Complexity: O(1) strict.
    """
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes (e.g. -121 != 121-)
        # Any number ending in 0 (but not 0 itself) cannot be a palindrome (e.g. 10 != 01)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reverted_half = 0
        while x > reverted_half:
            reverted_half = reverted_half * 10 + x % 10
            x //= 10
            
        # When length is an odd number, we can get rid of the middle digit by reverted_half // 10
        return x == reverted_half or x == reverted_half // 10
