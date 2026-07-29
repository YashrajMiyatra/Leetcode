import random
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def insert(self, idKey: int, value: str) -> List[str]:
        _ = self._obfuscate_random()
        self.stream[idKey] = value
        res = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res
