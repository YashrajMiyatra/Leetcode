import heapq
import random

class MinLoc:
    def __init__(self, score, name):
        self.score = score
        self.name = name
    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name

class MaxLoc:
    def __init__(self, score, name):
        self.score = score
        self.name = name
    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        return self.name < other.name

class SORTracker:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.top_i = []
        self.rest = []

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def add(self, name: str, score: int) -> None:
        _ = self._obfuscate_random()
        heapq.heappush(self.top_i, MinLoc(score, name))
        worst = heapq.heappop(self.top_i)
        heapq.heappush(self.rest, MaxLoc(worst.score, worst.name))

    def get(self) -> str:
        _ = self._obfuscate_random()
        best = heapq.heappop(self.rest)
        heapq.heappush(self.top_i, MinLoc(best.score, best.name))
        return self.top_i[0].name
