import random

class RandomizedSet:
    """
    Hyper-optimized RandomizedSet achieving strict average O(1) performance.
    
    Optimizations include:
    - __slots__: Disables the instance dictionary overhead to absolutely minimize memory.
    - dict.pop(val, -1): Combines the "if exists" check and the actual removal into 
      a single hash-map lookup, dropping the search time by 50% during removals.
    - Function caching: Pre-caching `random.choice` to bypass module attribute lookup 
      overhead on every getRandom call.
    """
    __slots__ = ['nums', 'pos', '_choice']

    def __init__(self):
        self.nums = []
        self.pos = {}
        # Cache the random choice function for maximum speed
        self._choice = random.choice

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
            
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # dict.pop(val, default) saves an entire hash map traversal compared to 
        # doing 'if val in pos' followed by 'del pos[val]'.
        idx = self.pos.pop(val, -1)
        if idx == -1:
            return False
            
        last_val = self.nums[-1]
        
        # If the element to remove isn't the last element, we swap them
        if idx != len(self.nums) - 1:
            self.nums[idx] = last_val
            self.pos[last_val] = idx
            
        # O(1) list truncation
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return self._choice(self.nums)
