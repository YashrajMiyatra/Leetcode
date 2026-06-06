class Solution:
    def integerReplacement(self, n: int) -> int:
        ops = 0
        while n > 1:
            # 1. If even, always divide by 2
            if n % 2 == 0:
                n //= 2
            # 2. If odd, decide whether to add or subtract 1:
            # - For n = 3, always subtract 1 (3 -> 2 -> 1 is optimal)
            # - If n % 4 == 1, subtracting 1 yields a multiple of 4, which is optimal
            elif n == 3 or n % 4 == 1:
                n -= 1
            # - If n % 4 == 3, adding 1 yields a multiple of 4, which is optimal
            else:
                n += 1
            ops += 1
            
        return ops
