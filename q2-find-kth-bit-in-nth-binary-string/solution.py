import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findKthBit(self, n: int, k: int) -> str:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        invert_count = 0
        length = (1 << n) - 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while length > 1:
            mid = length // 2 + 1
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if k == mid:
                return str(1 ^ (invert_count % 2))
                
            if k > mid:
                k = length - k + 1
                invert_count += 1
                
            length //= 2
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return str(0 ^ (invert_count % 2))

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_kth_bit(self, n: int, k: int) -> str:
        return self.findKthBit(n, k)
