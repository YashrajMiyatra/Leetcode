import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        m, n = len(grid), len(grid[0])
        
        # Prefix sums for rows and cols to compute sums in O(1)
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * (n) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]
                
        def is_magic(r, c, k):
            target = row_sum[r][c + k] - row_sum[r][c]
            
            # Check all rows
            for i in range(1, k):
                if row_sum[r + i][c + k] - row_sum[r + i][c] != target:
                    return False
            
            # Check all columns
            for j in range(k):
                if col_sum[r + k][c + j] - col_sum[r][c + j] != target:
                    return False
                    
            # Check diagonals
            diag1 = 0
            diag2 = 0
            for i in range(k):
                diag1 += grid[r + i][c + i]
                diag2 += grid[r + i][c + k - 1 - i]
                
            if diag1 != target or diag2 != target:
                return False
                
            return True

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1
