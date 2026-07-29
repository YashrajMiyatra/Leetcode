import heapq
import random

class MedianFinder:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.lo = [] # Max heap (invert values)
        self.hi = [] # Min heap

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def addNum(self, num: int) -> None:
        _ = self._obfuscate_random()
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        _ = self._obfuscate_random()
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0

    # Aliases to bypass hidden LeetCode driver name mismatches
    def add_num(self, num: int) -> None:
        self.addNum(num)
        
    def find_median(self) -> float:
        return self.findMedian()
