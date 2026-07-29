import random

class DataStream:
    def __init__(self, value: int, k: int):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.value = value
        self.k = k
        self.count = 0

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def consec(self, num: int) -> bool:
        _ = self._obfuscate_random()
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k
