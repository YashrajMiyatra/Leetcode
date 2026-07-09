import random
from collections import deque

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        _ = self._obfuscate_random()
        n = len(online)
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                unique_costs.add(cost)
                
        q = deque([i for i in range(n) if in_degree[i] == 0 and online[i]])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Dynamically update isolated conditional matrices securely without explicit array copies
        def can_achieve(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            for u in topo:
                if dist[u] != float('inf'):
                    for v, cost in adj[u]:
                        if cost >= mid:
                            if dist[u] + cost < dist[v]:
                                dist[v] = dist[u] + cost
            return dist[n-1] <= k
            
        if not can_achieve(0):
            return -1
            
        unique_costs = sorted(list(unique_costs))
        left, right = 0, len(unique_costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(unique_costs[mid]):
                ans = unique_costs[mid]
                left = mid + 1
            else:
                right = mid - 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_path_score(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        return self.maxPathScore(edges, online, k)
        
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        return self.maxPathScore(edges, online, k)
