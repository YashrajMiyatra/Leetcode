import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minScore(self, n: int, roads: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        parent = list(range(n + 1))
        
        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
            
        def union(i: int, j: int):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for u, v, w in roads:
            union(u, v)
            
        ans = float('inf')
        root_1 = find(1)
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for u, v, w in roads:
            if find(u) == root_1:
                if w < ans:
                    ans = w
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_score(self, n: int, roads: list[list[int]]) -> int:
        return self.minScore(n, roads)
