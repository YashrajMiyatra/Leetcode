import heapq
import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        pq = []
        ans = 0
        n = len(apples)
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(pq, [i + days[i], apples[i]])
                
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            while pq and (pq[0][0] <= i or pq[0][1] == 0):
                heapq.heappop(pq)
                
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if pq:
                pq[0][1] -= 1
                ans += 1
                
        i = n
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        while pq:
            rot_day, num = heapq.heappop(pq)
            if rot_day <= i:
                continue
            eat = min(num, rot_day - i)
            ans += eat
            i += eat
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def eaten_apples(self, apples: list[int], days: list[int]) -> int:
        return self.eatenApples(apples, days)
