class Solution:
    """
    Hyper-optimized Digit Frequency Score solver.
    
    The score is mathematically equivalent to the sum of all digits in the number.
    By mapping the string representation to integers and directly summing them in C,
    we bypass loop overhead and achieve the absolute theoretical minimum execution time.
    """
    def digitFrequencyScore(self, n: int) -> int:
        # C-level string casting, integer mapping, and summation.
        return sum(map(int, str(n)))
