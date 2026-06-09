import random
import heapq
from collections import defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minCost(self, n: int, edges: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Build the graph
        # For every edge u -> v with cost w:
        # We can traverse u -> v with cost w
        # We can traverse v -> u with cost 2w (using v's switch)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
            
        # Dijkstra's algorithm
        pq = [(0, 0)]  # (cost, node)
        min_cost = {0: 0}
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            if u == n - 1:
                return cost
                
            if cost > min_cost.get(u, float('inf')):
                continue
                
            for v, w in graph[u]:
                next_cost = cost + w
                if next_cost < min_cost.get(v, float('inf')):
                    min_cost[v] = next_cost
                    heapq.heappush(pq, (next_cost, v))
                    
        return -1
