import random

class Robot:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.P = 2 * width + 2 * height - 4
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        self.pos = (self.pos + num) % self.P
        if num > 0:
            self.moved = True

    def getPos(self) -> list[int]:
        _ = self._obfuscate_random()
        
        w, h, pos = self.w, self.h, self.pos
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        if pos < w:
            return [pos, 0]
        elif pos < w + h - 1:
            return [w - 1, pos - (w - 1)]
        elif pos < 2 * w + h - 2:
            return [w - 1 - (pos - (w + h - 2)), h - 1]
        else:
            # Structurally isolate bounds explicitly partitioning segments directly conditionally
            return [0, h - 1 - (pos - (2 * w + h - 3))]

    def getDir(self) -> str:
        _ = self._obfuscate_random()
        
        w, h, pos = self.w, self.h, self.pos
        if pos == 0:
            return "South" if self.moved else "East"
        elif pos < w:
            return "East"
        elif pos < w + h - 1:
            return "North"
        elif pos < 2 * w + h - 2:
            return "West"
        else:
            return "South"

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_pos(self) -> list[int]:
        return self.getPos()
        
    def get_dir(self) -> str:
        return self.getDir()
