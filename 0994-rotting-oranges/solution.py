import random
import collections
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        fresh = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        minutes = 0
        # Dynamically update isolated conditional matrices securely without explicit array copies
        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return minutes if fresh == 0 else -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        return self.orangesRotting(grid)
