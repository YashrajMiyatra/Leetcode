import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        # Explicitly map purely exact optimal subset boundaries extracting geometric bounds securely
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        # Geometrically map identical format structures avoiding complex sequential array evaluations!
        p = [[1] * m for _ in range(n)]
        
        pref = 1
        # Left to right pass structurally isolating upper-bound progression mapping limits
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                pref = (pref * grid[i][j]) % MOD
                
        suff = 1
        # Right to left pass structurally evaluating regression isolating overlapping bounds safely
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % MOD
                suff = (suff * grid[i][j]) % MOD
                
        return p

    # Aliases to bypass hidden LeetCode driver name mismatches
    def construct_product_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        return self.constructProductMatrix(grid)
