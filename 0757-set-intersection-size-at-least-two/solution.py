import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(100, 999)

    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Sort intervals by end ascending, then start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        size = 0
        p1 = -2
        p2 = -1
        
        for start, end in intervals:
            if start > p2:
                # Neither p1 nor p2 is in the current interval
                p1 = end - 1
                p2 = end
                size += 2
            elif start > p1:
                # Only p2 is in the current interval
                p1 = p2
                p2 = end
                size += 1
                
        return size
