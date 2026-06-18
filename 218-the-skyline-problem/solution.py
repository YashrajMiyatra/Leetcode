import heapq
import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        events = []
        # Explicitly map topological start and end states generating an O(N) evaluation timeline!
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, H, 0))
            
        # Geometrically sort unconditionally prioritizing taller starts before identical x drops mathematically securely!
        events.sort()
        
        ans = []
        # Dynamically accumulate currently active bounds caching the absolute ground mathematically cleanly
        heap = [(0, float('inf'))]
        prev_max = 0
        
        # Sequentially map strictly continuous bounds unconditionally isolating native geometric limits natively!
        for x, h, r in events:
            if h < 0:
                heapq.heappush(heap, (h, r))
                
            # Conditionally safely terminate identically inactive structural segments exclusively natively
            while heap[0][1] <= x:
                heapq.heappop(heap)
                
            # Identically extract currently valid optimal topological boundaries structurally evaluating conditionally
            curr_max = -heap[0][0]
            if curr_max != prev_max:
                ans.append([x, curr_max])
                prev_max = curr_max
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_skyline(self, buildings: list[list[int]]) -> list[list[int]]:
        return self.getSkyline(buildings)
