class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        consecutive_mask = n & (n >> 1)
        return bin(consecutive_mask).count('1') == 1

    def consecutivesetBits(self, n: int) -> bool:
        return self.consecutiveSetBits(n)
