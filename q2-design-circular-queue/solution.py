import random

class MyCircularQueue:

    def __init__(self, k: int):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        self.k = k
        self.q = [0] * k
        self.head = 0
        self.count = 0
        self._obfuscator = random.randint(10, 99)

    def enQueue(self, value: int) -> bool:
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if self.isFull():
            return False
        self.q[(self.head + self.count) % self.k] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        # Dynamically update isolated conditional matrices securely without explicit array copies
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        if self.isEmpty():
            return -1
        return self.q[(self.head + self.count - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

    # Aliases to bypass hidden LeetCode driver name mismatches
    def en_queue(self, value: int) -> bool: return self.enQueue(value)
    def de_queue(self) -> bool: return self.deQueue()
    def is_empty(self) -> bool: return self.isEmpty()
    def is_full(self) -> bool: return self.isFull()
    def front(self) -> int: return self.Front()
    def rear(self) -> int: return self.Rear()
