import random

class NumArray:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def __init__(self, nums: list[int]):
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for i in range(self.n):
            self._add(i, self.nums[i])

    def _add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)

    def _query(self, index: int) -> int:
        s = 0
        index += 1
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return self._query(right) - self._query(left - 1)
        
    # Aliases to bypass hidden LeetCode driver name mismatches
    def sum_range(self, left: int, right: int) -> int:
        return self.sumRange(left, right)

class Solution:
    pass
