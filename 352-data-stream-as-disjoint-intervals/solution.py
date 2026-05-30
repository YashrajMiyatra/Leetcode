class SummaryRanges:
    """
    Optimized SummaryRanges class.
    
    The constraints indicate `addNum` is called heavily (up to 30,000 times), 
    while `getIntervals` is called extremely rarely (at most 100 times).
    
    Instead of actively maintaining and merging a sorted list of intervals on 
    every insertion (which creates massive overhead due to Python list shifting), 
    we employ Lazy Evaluation.
    
    We just dump numbers into a Python `set()` which inserts in pure C at O(1) speed.
    When `getIntervals` is requested, we sort the set in C using `sorted()` and do 
    a fast linear sweep to group the intervals.
    """
    __slots__ = ['seen']

    def __init__(self):
        self.seen = set()

    def addNum(self, value: int) -> None:
        # O(1) hash set insertion
        self.seen.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.seen:
            return []
            
        # sorted() is executed in C, making it extremely fast
        nums = sorted(self.seen)
        res = []
        
        start = end = nums[0]
        
        # Fast linear grouping loop
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                res.append([start, end])
                start = end = n
                
        res.append([start, end])
        return res
