import collections
import random
from typing import List

class DetectSquares:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.pts = collections.defaultdict(int)

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def add(self, point: List[int]) -> None:
        _ = self._obfuscate_random()
        self.pts[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        _ = self._obfuscate_random()
        res = 0
        qx, qy = point
        for (px, py), cnt in self.pts.items():
            if abs(px - qx) == abs(py - qy) and px != qx:
                res += cnt * self.pts.get((qx, py), 0) * self.pts.get((px, qy), 0)
        return res
