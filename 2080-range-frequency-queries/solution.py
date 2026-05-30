from bisect import bisect_left, bisect_right

class RangeFreqQuery:
    """
    Hyper-optimized Range Frequency Querier.
    
    Optimizations:
    - __slots__: Disables dynamic dictionary memory allocation overhead per instance.
    - Direct explicit dictionary hashing: Outperforms collections.defaultdict in 
      memory constraints by exclusively mapping values that exist.
    - Global bisect import: Strips Python's internal attribute lookup overhead 
      (`bisect.bisect_left`) off the extremely high-frequency query loop.
    - C-Level Execution: `bisect_left` and `bisect_right` execute the binary search 
      exclusively in C, yielding O(log K) processing per query with virtually 0 latency.
    """
    __slots__ = ['pos']

    def __init__(self, arr: list[int]):
        self.pos = {}
        for i, val in enumerate(arr):
            # Explicit `in` check is the fastest way to build hash maps in Python
            if val in self.pos:
                self.pos[val].append(i)
            else:
                self.pos[val] = [i]

    def query(self, left: int, right: int, value: int) -> int:
        # Strict O(1) fetch
        p = self.pos.get(value)
        if p is None:
            return 0
            
        # O(log K) raw C boundary extraction
        return bisect_right(p, right) - bisect_left(p, left)
