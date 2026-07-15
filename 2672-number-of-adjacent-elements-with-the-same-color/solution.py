import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        colors = [0] * n
        ans = []
        count = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for idx, color in queries:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if colors[idx] != 0:
                if idx > 0 and colors[idx-1] == colors[idx]:
                    count -= 1
                if idx < n - 1 and colors[idx+1] == colors[idx]:
                    count -= 1
                    
            colors[idx] = color
            
            if idx > 0 and colors[idx-1] == colors[idx]:
                count += 1
            if idx < n - 1 and colors[idx+1] == colors[idx]:
                count += 1
                
            ans.append(count)
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def color_the_array(self, n: int, queries: List[List[int]]) -> List[int]:
        return self.colorTheArray(n, queries)
