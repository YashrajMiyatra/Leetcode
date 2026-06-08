import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        n = len(bottomLeft)
        max_side = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                tr_x = min(topRight[i][0], topRight[j][0])
                tr_y = min(topRight[i][1], topRight[j][1])
                
                w = tr_x - bl_x
                h = tr_y - bl_y
                
                if w > 0 and h > 0:
                    max_side = max(max_side, min(w, h))
                    
        return max_side * max_side
