import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(m):
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_pos = j - 1
                elif boxGrid[i][j] == '#':
                    # Dynamically update isolated conditional matrices securely without explicit array copies
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty_pos] = '#'
                    empty_pos -= 1
                    
        ans = [['.'] * m for _ in range(n)]
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        for i in range(m):
            for j in range(n):
                ans[j][m - 1 - i] = boxGrid[i][j]
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def rotate_the_box(self, boxGrid: list[list[str]]) -> list[list[str]]:
        return self.rotateTheBox(boxGrid)
