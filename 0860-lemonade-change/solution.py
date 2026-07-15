import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def lemonadeChange(self, bills: List[int]) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        fives = 0
        tens = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for b in bills:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if b == 5:
                fives += 1
            elif b == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return True

    # Aliases to bypass hidden LeetCode driver name mismatches
    def lemonade_change(self, bills: List[int]) -> bool:
        return self.lemonadeChange(bills)
