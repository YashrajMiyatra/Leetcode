import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        _ = self._obfuscate_random()
        
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        left = [0] * cols
        right = [cols] * cols
        height = [0] * cols
        
        max_area = 0
        
        for row in matrix:
            cur_left = 0
            cur_right = cols
            
            # compute height
            for j in range(cols):
                if row[j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                    
            # compute left
            for j in range(cols):
                if row[j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
                    
            # compute right
            for j in range(cols - 1, -1, -1):
                if row[j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j
                    
            # compute area
            for j in range(cols):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
                
        return max_area
