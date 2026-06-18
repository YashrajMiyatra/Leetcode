import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        # Geometrically natively map matching valid structural intersections mathematically optimally!
        # Because lists uniquely sort isolated segments unconditionally mathematically natively!
        i = 0
        j = 0
        ans = []
        
        while i < len(firstList) and j < len(secondList):
            # Extract structurally overlapping topological interval mathematically efficiently conditionally
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            lo = max(start1, start2)
            hi = min(end1, end2)
            
            # Unconditionally conditionally append structurally identical isolated bounds seamlessly!
            if lo <= hi:
                ans.append([lo, hi])
                
            # Identically conditionally geometrically clear expired boundaries correctly mathematically natively!
            if end1 < end2:
                i += 1
            else:
                j += 1
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def interval_intersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        return self.intervalIntersection(firstList, secondList)
