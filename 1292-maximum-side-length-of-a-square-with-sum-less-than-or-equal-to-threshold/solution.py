import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        _ = self._obfuscate_random()
        
        m, n = len(mat), len(mat[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_k = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + mat[i-1][j-1]
                
                # Check if a square of size max_k + 1 ending at (i, j) is valid
                if i > max_k and j > max_k:
                    k = max_k + 1
                    r1, c1 = i - k, j - k
                    curr_sum = pref[i][j] - pref[r1][j] - pref[i][c1] + pref[r1][c1]
                    
                    if curr_sum <= threshold:
                        max_k = k
                        
        return max_k
