import bisect

class RangeModule:
    """
    Hyper-optimized 1D Array Segment Tree approach.
    
    Instead of building an actual node-based Segment Tree which suffers from 
    massive recursive and object overhead, we maintain a flat 1D array `X`.
    Even indices represent interval starts, odd indices represent interval ends.
    
    Python's `bisect` runs natively in C. 
    Python's array slice assignment `self.X[i:j] = sub` runs natively in C.
    
    This flattens what normally takes 50+ lines of complex tree rebalancing 
    into 4 lines of pure C-level binary searching and memory slicing, destroying
    the execution percentiles.
    """
    __slots__ = ['X']

    def __init__(self):
        self.X = []

    def addRange(self, left: int, right: int) -> None:
        # bisect_left / bisect_right binary search in pure C
        i = bisect.bisect_left(self.X, left)
        j = bisect.bisect_right(self.X, right)
        
        # Determine if we need to inject the start/end points or if they 
        # seamlessly merge into an existing interval block
        sub = []
        if i % 2 == 0:
            sub.append(left)
        if j % 2 == 0:
            sub.append(right)
            
        # O(K) C-level memory slice replacement
        self.X[i:j] = sub

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.X, left)
        j = bisect.bisect_left(self.X, right)
        # If they fall in the exact same interval (i == j) and it's 
        # inside a tracked block (i % 2 == 1), then it's fully covered.
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.X, left)
        j = bisect.bisect_right(self.X, right)
        
        sub = []
        if i % 2 == 1:
            sub.append(left)
        if j % 2 == 1:
            sub.append(right)
            
        self.X[i:j] = sub
