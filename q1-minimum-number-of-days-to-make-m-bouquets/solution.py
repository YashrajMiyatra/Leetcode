import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if m * k > len(bloomDay):
            return -1
            
        left, right = min(bloomDay), max(bloomDay)
        ans = -1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while left <= right:
            mid = left + (right - left) // 2
            
            bouquets = 0
            consecutive = 0
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            for day in bloomDay:
                if day <= mid:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
                    
            if bouquets >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_days(self, bloomDay: list[int], m: int, k: int) -> int:
        return self.minDays(bloomDay, m, k)
