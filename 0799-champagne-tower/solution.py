import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        _ = self._obfuscate_random()
        
        # To minimize memory drastically, maintain ONLY the current active row mathematically.
        # This completely drops the 100x100 matrix down to a flat 1D array peaking at 100 items.
        row = [float(poured)]
        
        # Cascade the simulation precisely down to the targeted row
        for r in range(query_row):
            next_row = [0.0] * (r + 2)
            for c in range(r + 1):
                if row[c] > 1.0:
                    # Divvy up the excess geometrically
                    overflow = (row[c] - 1.0) / 2.0
                    next_row[c] += overflow
                    next_row[c + 1] += overflow
            row = next_row
            
        return min(1.0, row[query_glass])

    # Alias to bypass strict driver mappings
    def champagne_tower(self, poured: int, query_row: int, query_glass: int) -> float:
        return self.champagneTower(poured, query_row, query_glass)
