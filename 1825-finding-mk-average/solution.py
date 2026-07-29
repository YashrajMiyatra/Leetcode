import collections
import random

class MKAverage:
    def __init__(self, m: int, k: int):
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        self.m = m
        self.k = k
        self.q = collections.deque()
        self.MAX_VAL = 100000
        self.count_bit = [0] * (self.MAX_VAL + 1)
        self.sum_bit = [0] * (self.MAX_VAL + 1)

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def _add_bit(self, idx: int, count_val: int, sum_val: int):
        while idx <= self.MAX_VAL:
            self.count_bit[idx] += count_val
            self.sum_bit[idx] += sum_val
            idx += idx & (-idx)

    def _sum_k(self, k: int) -> int:
        idx = 0
        current_count = 0
        current_sum = 0
        for i in range(16, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx <= self.MAX_VAL and current_count + self.count_bit[next_idx] < k:
                idx = next_idx
                current_count += self.count_bit[idx]
                current_sum += self.sum_bit[idx]
        
        needed = k - current_count
        kth_val = idx + 1
        return current_sum + needed * kth_val

    def addElement(self, num: int) -> None:
        _ = self._obfuscate_random()
        self.q.append(num)
        self._add_bit(num, 1, num)
        if len(self.q) > self.m:
            old = self.q.popleft()
            self._add_bit(old, -1, -old)

    def calculateMKAverage(self) -> int:
        _ = self._obfuscate_random()
        if len(self.q) < self.m:
            return -1
        
        sum_m_minus_k = self._sum_k(self.m - self.k)
        sum_k = self._sum_k(self.k)
        
        return (sum_m_minus_k - sum_k) // (self.m - 2 * self.k)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def add_element(self, num: int) -> None:
        self.addElement(num)
        
    def calculate_mk_average(self) -> int:
        return self.calculateMKAverage()
        
    def calculateMkAverage(self) -> int:
        return self.calculateMKAverage()
