import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def monotoneIncreasingDigits(self, n: int) -> int:
        _ = self._obfuscate_random()
        
        digits = list(str(n))
        marker = len(digits)
        
        # Traverse the number from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                marker = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                
        # Set all digits from the marker to the end to '9'
        for i in range(marker, len(digits)):
            digits[i] = '9'
            
        return int("".join(digits))
