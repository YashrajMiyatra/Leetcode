from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
                
        # If there is at least one odd count, we can place one odd element in the center
        return length + 1 if has_odd else length
