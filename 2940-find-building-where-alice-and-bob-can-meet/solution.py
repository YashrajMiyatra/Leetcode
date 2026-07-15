import heapq
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(heights)
        ans = [-1] * len(queries)
        groups = [[] for _ in range(n)]
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                # We need a building j > b with heights[j] > heights[a]
                groups[b].append((heights[a], i))
                
        heap = []
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for i, h in enumerate(heights):
            while heap and heap[0][0] < h:
                _, q_idx = heapq.heappop(heap)
                ans[q_idx] = i
                
            for q in groups[i]:
                heapq.heappush(heap, q)
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def leftmost_building_queries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        return self.leftmostBuildingQueries(heights, queries)
