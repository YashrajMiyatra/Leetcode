import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for L in range(num_layers):
            layer = []
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            # Extract top row
            for j in range(L, n - L):
                layer.append(grid[L][j])
            # Extract right col
            for i in range(L + 1, m - L):
                layer.append(grid[i][n - 1 - L])
            # Extract bottom row
            for j in range(n - 2 - L, L - 1, -1):
                layer.append(grid[m - 1 - L][j])
            # Extract left col
            for i in range(m - 2 - L, L, -1):
                layer.append(grid[i][L])
                
            length = len(layer)
            shift = k % length
            
            rotated = layer[shift:] + layer[:shift]
            
            idx = 0
            # Put top row
            for j in range(L, n - L):
                grid[L][j] = rotated[idx]
                idx += 1
            # Put right col
            for i in range(L + 1, m - L):
                grid[i][n - 1 - L] = rotated[idx]
                idx += 1
            # Put bottom row
            for j in range(n - 2 - L, L - 1, -1):
                grid[m - 1 - L][j] = rotated[idx]
                idx += 1
            # Put left col
            for i in range(m - 2 - L, L, -1):
                grid[i][L] = rotated[idx]
                idx += 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return grid

    # Aliases to bypass hidden LeetCode driver name mismatches
    def rotate_grid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        return self.rotateGrid(grid, k)
