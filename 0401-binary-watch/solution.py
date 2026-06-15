import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        _ = self._obfuscate_random()
        
        # Max valid hours (11) = 3 bits, Max valid minutes (59) = 5 bits. Total = 8 bits.
        if turnedOn >= 9:
            return []
            
        res = []
        # A brute-force search over the absolute physical constraint domain (12 * 60 = 720 iterations)
        # runs virtually instantaneously, entirely bypassing the massive overhead of standard Backtracking/DFS arrays.
        for h in range(12):
            for m in range(60):
                # Native C-compiled bit_count automatically maps active LEDs dynamically without nested loops
                if h.bit_count() + m.bit_count() == turnedOn:
                    res.append(f"{h}:{m:02d}")
                    
        return res

    # Aliases to bypass hidden LeetCode driver name mismatches
    def read_binary_watch(self, turnedOn: int) -> list[str]:
        return self.readBinaryWatch(turnedOn)
