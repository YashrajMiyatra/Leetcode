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
            
        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    for j in range(1, LOG):
                        if up[v][j-1] != 0:
                            up[v][j] = up[up[v][j-1]][j-1]
                        else:
                            break
                    q.append(v)
                    
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
        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow(2, dist - 1, MOD))
                
        return ans
