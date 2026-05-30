import random

class RandomizedCollection:
    """
    Ultra-optimized RandomizedCollection for duplicates handling.
    
    Optimizations include:
    - __slots__: Disables dynamic dictionary overhead for maximum memory constraint.
    - dict with Sets: Uses a hash map of sets for strictly O(1) indices management.
    - Conditional Deletion: Garbage-collects empty sets instantly `del self.pos[val]`
      so Python's memory footprint never continuously inflates.
    - Function caching: Pre-caching `random.choice`.
    """
    __slots__ = ['nums', 'pos', '_choice']

    def __init__(self):
        self.nums = []
        self.pos = {}
        # Pre-cache random choice to avoid runtime module lookups
        self._choice = random.choice

    def insert(self, val: int) -> bool:
        indices = self.pos.get(val)
        is_not_present = not indices
        
        # If it's totally missing, initialize a C-level hash set for it
        if is_not_present:
            indices = set()
            self.pos[val] = indices
            
        indices.add(len(self.nums))
        self.nums.append(val)
        return is_not_present

    def remove(self, val: int) -> bool:
        indices = self.pos.get(val)
        if not indices:
            return False
            
        # O(1) pop from set
        remove_idx = indices.pop()
        last_idx = len(self.nums) - 1
        
        # Aggressively delete empty sets to prevent memory ballooning
        if not indices:
            del self.pos[val]
            
        # If we aren't already removing the last element, swap them
        if remove_idx != last_idx:
            last_val = self.nums[-1]
            self.nums[remove_idx] = last_val
            
            # Update the swapped element's index reference
            last_indices = self.pos[last_val]
            last_indices.remove(last_idx)
            last_indices.add(remove_idx)
            
        # Strictly O(1) list truncation
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return self._choice(self.nums)
