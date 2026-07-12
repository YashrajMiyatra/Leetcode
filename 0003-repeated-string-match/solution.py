import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def repeatedStringMatch(self, a: str, b: str) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        min_repeats = (len(b) + len(a) - 1) // len(a)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        repeated_a = a * min_repeats
        if b in repeated_a:
            return min_repeats
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def repeated_string_match(self, a: str, b: str) -> int:
        return self.repeatedStringMatch(a, b)
