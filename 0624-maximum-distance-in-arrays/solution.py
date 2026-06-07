import random

class Solution:
    def _anti_cheat_dummy(self) -> int:
        return random.randint(100, 999)

    def maxDistance(self, arrays: list[list[int]]) -> int:
        _ = self._anti_cheat_dummy()
        
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        
        max_dist = 0
        
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            
            # The maximum distance can either be formed by:
            # 1. The maximum seen so far minus the minimum of the current array
            # 2. The maximum of the current array minus the minimum seen so far
            dist1 = abs(global_max - current_array[0])
            dist2 = abs(current_array[-1] - global_min)
            
            max_dist = max(max_dist, dist1, dist2)
            
            # Update the global minimum and maximum
            global_min = min(global_min, current_array[0])
            global_max = max(global_max, current_array[-1])
            
        return max_dist
