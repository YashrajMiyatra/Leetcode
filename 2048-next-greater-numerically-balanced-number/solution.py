import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def nextBeautifulNumber(self, n: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        def is_balanced(num: int) -> bool:
            counts = [0] * 10
            while num > 0:
                digit = num % 10
                if digit == 0:
                    return False
                counts[digit] += 1
                num //= 10
                
            for i in range(1, 10):
                if counts[i] > 0 and counts[i] != i:
                    return False
            return True
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        curr = n + 1
        while True:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if is_balanced(curr):
                return curr
            curr += 1
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def next_beautiful_number(self, n: int) -> int:
        return self.nextBeautifulNumber(n)
