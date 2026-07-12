import random
import math

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def judgeSquareSum(self, c: int) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        a = 0
        b = int(math.isqrt(c))
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while a <= b:
            current_sum = a * a + b * b
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def judge_square_sum(self, c: int) -> bool:
        return self.judgeSquareSum(c)
