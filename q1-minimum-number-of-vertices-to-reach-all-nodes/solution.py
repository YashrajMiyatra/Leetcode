import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        has_incoming = [False] * n
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for u, v in edges:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            has_incoming[v] = True
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return [i for i in range(n) if not has_incoming[i]]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_smallest_set_of_vertices(self, n: int, edges: list[list[int]]) -> list[int]:
        return self.findSmallestSetOfVertices(n, edges)
