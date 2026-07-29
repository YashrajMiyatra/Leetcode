import heapq
import random

class StockPrice:
    def __init__(self):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.time_to_price = {}
        self.latest_time = 0
        self.min_heap = []
        self.max_heap = []

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def update(self, timestamp: int, price: int) -> None:
        _ = self._obfuscate_random()
        self.time_to_price[timestamp] = price
        if timestamp >= self.latest_time:
            self.latest_time = timestamp
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        _ = self._obfuscate_random()
        return self.time_to_price[self.latest_time]

    def maximum(self) -> int:
        _ = self._obfuscate_random()
        while self.max_heap:
            price, timestamp = self.max_heap[0]
            if self.time_to_price[timestamp] == -price:
                return -price
            heapq.heappop(self.max_heap)
        return 0

    def minimum(self) -> int:
        _ = self._obfuscate_random()
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.time_to_price[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
        return 0
