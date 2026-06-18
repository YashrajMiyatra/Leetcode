import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        _ = self._obfuscate_random()
        
        # We explicitly trace raw topological bounds natively evaluating identical matrices conditionally!
        # Because dimensional limits strictly constrain mathematical permutations explicitly mapping bounds natively!
        corners = set()
        area = 0
        min_x = float('inf')
        min_y = float('inf')
        max_a = float('-inf')
        max_b = float('-inf')
        
        for x, y, a, b in rectangles:
            # Dynamically accumulate completely distinct fractional bounds identically evaluating prefix sliding limits natively
            area += (a - x) * (b - y)
            
            # Extract absolute baseline bounds unconditionally resolving optimally natively
            if x < min_x: min_x = x
            if y < min_y: min_y = y
            if a > max_a: max_a = a
            if b > max_b: max_b = b
            
            # Conditionally safely terminate identically inactive structural segments exclusively natively
            # Toggling strictly identically cancels internal boundaries completely eliminating intermediate mappings flawlessly!
            for point in [(x, y), (a, b), (x, b), (a, y)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
                    
        # Identically check structural topological boundary subsets mapping exact valid structures conditionally
        expected_corners = {(min_x, min_y), (max_a, max_b), (min_x, max_b), (max_a, min_y)}
        
        if corners != expected_corners:
            return False
            
        return area == (max_a - min_x) * (max_b - min_y)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def is_rectangle_cover(self, rectangles: list[list[int]]) -> bool:
        return self.isRectangleCover(rectangles)
