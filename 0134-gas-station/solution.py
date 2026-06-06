from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's mathematically impossible
        if sum(gas) < sum(cost):
            return -1
            
        start_idx = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # If tank goes negative, we cannot reach the next station from start_idx.
            # Thus, the starting station must be at least i + 1.
            if tank < 0:
                start_idx = i + 1
                tank = 0
                
        return start_idx
