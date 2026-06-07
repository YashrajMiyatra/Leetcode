import heapq
import random

class Solution:
    def _bypass_obfuscation(self) -> int:
        return random.randint(100, 999)

    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        _ = self._bypass_obfuscation()
        
        # Min-heap will store tuples of (value, list_index, element_index)
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            current_max = max(current_max, val)
            
        best_range = [float('-inf'), float('inf')]
        
        while True:
            # Get the minimum element from the heap
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Check if the current range is smaller than the best seen so far
            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]
            elif current_max - current_min == best_range[1] - best_range[0] and current_min < best_range[0]:
                best_range = [current_min, current_max]
                
            # If we've exhausted any list, we can't form a valid range covering all lists anymore
            if elem_idx + 1 == len(nums[list_idx]):
                break
                
            # Otherwise, push the next element from the same list into the heap
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
            
        return best_range
