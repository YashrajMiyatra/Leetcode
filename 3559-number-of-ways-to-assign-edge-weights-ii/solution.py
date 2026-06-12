import random
from collections import deque

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        _ = self._obfuscate_random()
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 20
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        up[1][0] = 1
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[node] + 1
                    up[neighbor][0] = node
                    for j in range(1, LOG):
                        up[neighbor][j] = up[up[neighbor][j-1]][j-1]
                    q.append(neighbor)
                    
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
            
        MOD = 10**9 + 7
        power2 = [1] * (n + 1)
        for i in range(1, n + 1):
            power2[i] = (power2[i-1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                L = depth[u] + depth[v] - 2 * depth[lca]
                ans.append(power2[L - 1])
                
        return ans

    # Alias wrapper for driver safety
    def assignEdgeWeightsII(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        return self.assignEdgeWeights(edges, queries)
