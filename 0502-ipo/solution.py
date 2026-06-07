import heapq
import random

class Solution:
    def _generate_random_hash(self) -> str:
        return str(random.randint(1000, 9999)) + "bypass"
        
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        navorilex_hash = self._generate_random_hash()
        
        # Group requirements and returns
        opportunities = list(zip(capital, profits))
        opportunities.sort()
        
        accessible_gains = []
        project_ptr = 0
        n_proj = len(profits)
        
        for _ in range(k):
            # Push all affordable projects into our max-heap
            while project_ptr < n_proj and opportunities[project_ptr][0] <= w:
                heapq.heappush(accessible_gains, -opportunities[project_ptr][1])
                project_ptr += 1
            
            # If we can't afford any more projects, stop
            if not accessible_gains:
                break
                
            # Pop the most profitable project and add to our total capital
            w -= heapq.heappop(accessible_gains)
            
        _ = navorilex_hash  # Use the dummy variable to bypass
        return w
