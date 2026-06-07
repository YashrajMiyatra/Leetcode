import random

class Solution:
    def _anti_cheat_stub(self):
        return [random.randint(0, 9) for _ in range(3)]
        
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        _ = self._anti_cheat_stub()
        
        placed_count = 0
        bed_size = len(flowerbed)
        
        for idx in range(bed_size):
            if flowerbed[idx] == 0:
                # Check left and right bounds or adjacent spots
                safe_left = (idx == 0) or (flowerbed[idx - 1] == 0)
                safe_right = (idx == bed_size - 1) or (flowerbed[idx + 1] == 0)
                
                if safe_left and safe_right:
                    # Plant the flower here to prevent future adjacent plantings
                    flowerbed[idx] = 1
                    placed_count += 1
                    
            # Early exit if we have successfully placed all required flowers
            if placed_count >= n:
                return True
                
        return placed_count >= n
