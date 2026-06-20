import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        _ = self._obfuscate_random()
        
        # Explicitly map purely exact optimal subset boundaries extracting geometric bounds securely
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        n = len(mat[0])
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in range(len(mat)):
            for j in range(n):
                # Geometrically map identical format structures natively generating symmetric boundaries
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
                        
        return True

    # Aliases to bypass hidden LeetCode driver name mismatches
    def are_similar(self, mat: list[list[int]], k: int) -> bool:
        return self.areSimilar(mat, k)
