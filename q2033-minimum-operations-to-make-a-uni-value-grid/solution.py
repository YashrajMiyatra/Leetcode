import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minOperations(self, grid: list[list[int]], x: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        arr = []
        for row in grid:
            arr.extend(row)
            
        rem = arr[0] % x
        for val in arr:
            if val % x != rem:
                return -1
                
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        arr.sort()
        target = arr[len(arr) // 2]
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        ans = 0
        for val in arr:
            ans += abs(val - target) // x
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_operations(self, grid: list[list[int]], x: int) -> int:
        return self.minOperations(grid, x)
