import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        total_time = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time
