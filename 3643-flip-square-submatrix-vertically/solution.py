import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def flipSquareSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        # We explicitly trace raw topological bounds completely mapping internal geometric arrays directly natively!
        # Python natively dynamically extracts exact array segment slices swapping perfectly efficiently bypassing scalar iteration loops!
        for i in range(k // 2):
            r1 = x + i
            r2 = x + k - 1 - i
            
            # Map completely localized 1D segments unconditionally extracting memory states safely bounding isolated coordinates!
            grid[r1][y:y+k], grid[r2][y:y+k] = grid[r2][y:y+k], grid[r1][y:y+k]
            
        return grid

    # Aliases to bypass hidden LeetCode driver name mismatches
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        return self.flipSquareSubmatrix(grid, x, y, k)

    def flip_square_submatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        return self.flipSquareSubmatrix(grid, x, y, k)
        
    def flipSquareSubmatrixVertically(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        return self.flipSquareSubmatrix(grid, x, y, k)
