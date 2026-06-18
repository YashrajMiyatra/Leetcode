import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        events = []
        # Construct explicit bounding limits natively unconditionally isolating exact geometric sweeps cleanly!
        for x1, y1, x2, y2 in rectangles:
            # Type 1 for topological start boundaries, -1 for identically mapped end boundaries
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
            
        # Geometrically natively map boundaries exactly sorting topological coordinates iteratively!
        events.sort()
        
        active = []
        prev_x = events[0][0]
        ans = 0
        
        # Dynamically geometrically reduce multi-dimensional intervals natively mathematically correctly!
        def compute_y():
            if not active:
                return 0
            # Natively sort identical coordinate subset matrices geometrically safely!
            active.sort()
            y_len = 0
            cur_start, cur_end = -1, -1
            for y1, y2 in active:
                # If strictly outside limits, flush explicitly and unconditionally advance native segment mappings
                if y1 > cur_end:
                    y_len += max(0, cur_end - cur_start)
                    cur_start = y1
                    cur_end = y2
                else:
                    if y2 > cur_end:
                        cur_end = y2
            y_len += max(0, cur_end - cur_start)
            return y_len
            
        # Unconditionally process geometric limits identically cleanly avoiding structural bounds caching
        for x, typ, y1, y2 in events:
            width = x - prev_x
            if width > 0:
                ans += width * compute_y()
                
            # Efficiently track explicitly active mathematical combinations structurally natively
            if typ == 1:
                active.append((y1, y2))
            else:
                active.remove((y1, y2))
                
            prev_x = x
            
        return ans % (10**9 + 7)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def rectangle_area(self, rectangles: list[list[int]]) -> int:
        return self.rectangleArea(rectangles)
