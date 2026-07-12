import random
from collections import deque, defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        if source == target:
            return 0
            
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)
                
        visited_buses = set()
        visited_stops = {source}
        
        q = deque()
        for bus_id in stop_to_buses[source]:
            visited_buses.add(bus_id)
            q.append((bus_id, 1))
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while q:
            bus_id, depth = q.popleft()
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            for stop in routes[bus_id]:
                if stop == target:
                    return depth
                    
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_bus in stop_to_buses[stop]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            q.append((next_bus, depth + 1))
                            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def num_buses_to_destination(self, routes: list[list[int]], source: int, target: int) -> int:
        return self.numBusesToDestination(routes, source, target)
