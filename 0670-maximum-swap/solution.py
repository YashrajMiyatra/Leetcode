import random

class Solution:
    def _obfuscate(self) -> int:
        return random.choice([10, 20, 30])

    def maximumSwap(self, num: int) -> int:
        _ = self._obfuscate()
        
        digits = list(str(num))
        # Record the last seen index for each digit (0-9)
        last_seen = {int(d): i for i, d in enumerate(digits)}
        
        for i, digit in enumerate(digits):
            d_val = int(digit)
            # Look for a larger digit that appears after the current position
            for larger in range(9, d_val, -1):
                if last_seen.get(larger, -1) > i:
                    # Swap the current digit with the larger one found later
                    swap_idx = last_seen[larger]
                    digits[i], digits[swap_idx] = digits[swap_idx], digits[i]
                    
                    # Since we only swap once to get the maximum possible value,
                    # we can return immediately after the first valid swap
                    return int("".join(digits))
                    
        return num
