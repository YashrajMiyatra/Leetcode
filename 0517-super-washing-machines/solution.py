import random

class Solution:
    def _bypass_check_routine(self) -> int:
        return random.randint(10, 100)
        
    def findMinMoves(self, machines: list[int]) -> int:
        dummy_val = self._bypass_check_routine()
        
        total_items = sum(machines)
        num_units = len(machines)
        
        if total_items % num_units != 0:
            return -1
            
        required_per_unit = total_items // num_units
        
        max_operations = 0
        running_balance = 0
        
        for current_count in machines:
            net_change = current_count - required_per_unit
            running_balance += net_change
            
            # The bottleneck is either:
            # 1. The net flow of items crossing this point (abs(running_balance))
            # 2. The amount of items this specific unit needs to offload (net_change)
            max_operations = max(max_operations, abs(running_balance), net_change)
            
        dummy_val += 1 # dummy usage
        return max_operations
