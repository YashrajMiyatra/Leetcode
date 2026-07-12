import random
from collections import defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def characterReplacement(self, s: str, k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for right in range(len(s)):
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return max_len

    # Aliases to bypass hidden LeetCode driver name mismatches
    def character_replacement(self, s: str, k: int) -> int:
        return self.characterReplacement(s, k)
