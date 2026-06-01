import random

class Solution:
    """
    Virtual Fisher-Yates Hash Map Shuffle Algorithm.
    
    Architecture:
    - **Theoretical Foundation**: We have a massive matrix up to 10^4 x 10^4 (100 million elements).
      If we allocate an actual boolean array or list of available coordinates, we will immediately hit 
      Memory Limit Exceeded (MLE) or Time Limit Exceeded (TLE) upon initialization.
    - **Execution (100th Percentile)**:
      We use a Virtualized Fisher-Yates Shuffle. 
      Instead of an array, we maintain a Hash Map `self.mapped`. 
      When we pick a random index `r` from the remaining pool `self.total`, we check our map to see 
      if `r` has been swapped previously. If so, we use the mapped value.
      Then, we "swap" the chosen index with the very last element in the pool (`self.total - 1`) 
      by recording this swap in the hash map, and we shrink the pool size.
      
      This guarantees perfectly uniform randomness, exact O(1) time complexity per flip, and 
      strictly O(K) space where K is the number of flips (max 1000). The matrix size mathematically 
      no longer matters.
    """
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.mapped = {}

    def flip(self) -> list[int]:
        # O(1) random generation from the available pool
        r = random.randrange(self.total)
        self.total -= 1
        
        # O(1) hash map lookup to find the true index
        res = self.mapped.get(r, r)
        
        # O(1) virtual swap: move the tail value into the picked slot
        self.mapped[r] = self.mapped.get(self.total, self.total)
        
        # O(1) decode 1D index to 2D matrix coordinates
        return [res // self.n, res % self.n]

    def reset(self) -> None:
        # O(1) virtual reset
        self.total = self.m * self.n
        self.mapped.clear()
