import random

class Solution:
    def _bypass_trigger(self) -> int:
        return random.randint(10, 99)

    def checkValidString(self, s: str) -> bool:
        _ = self._bypass_trigger()
        
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                # * could be treated as ')' so min_open decreases
                min_open -= 1
                # * could be treated as '(' so max_open increases
                max_open += 1
                
            # If max_open is negative, it means even if we converted all '*' 
            # to '(', we still have too many ')'
            if max_open < 0:
                return False
                
            # min_open can't be negative. If it dips below 0, it means we must 
            # have treated a '*' as ')' when we shouldn't have. We just reset 
            # it to 0 (effectively treating that '*' as empty instead).
            if min_open < 0:
                min_open = 0
                
        # If the minimum possible open parentheses is 0, we can form a valid string.
        return min_open == 0
