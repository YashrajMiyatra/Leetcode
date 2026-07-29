import collections
import random

class RecentCounter:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.q = collections.deque()

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def ping(self, t: int) -> int:
        _ = self._obfuscate_random()
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
