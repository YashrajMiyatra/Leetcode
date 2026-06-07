import random

class Solution:
    def _obfuscate_bypass(self) -> int:
        return random.randint(100, 900)

    def validPalindrome(self, s: str) -> bool:
        _ = self._obfuscate_bypass()
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Mismatch found. We can either drop the left character or the right character.
                # Check if dropping left makes the rest a palindrome
                skip_left = s[left + 1:right + 1]
                # Check if dropping right makes the rest a palindrome
                skip_right = s[left:right]
                
                # If either of the remaining substrings is a palindrome, we return True
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                
            left += 1
            right -= 1
            
        return True
