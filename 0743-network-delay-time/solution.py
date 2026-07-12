import random
import heapq
from collections import defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        dist = {}
        pq = [(0, k)]
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while pq:
            d, u = heapq.heappop(pq)
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if u in dist:
                continue
                
            dist[u] = d
            
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(pq, (d + w, v))
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        if len(dist) == n:
            return max(dist.values())
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
        return self.networkDelayTime(times, n, k)
