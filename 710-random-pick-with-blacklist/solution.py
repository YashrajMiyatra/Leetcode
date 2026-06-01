import random

class Solution:
    """
    Hyper-Optimized Hash Map Remapping Algorithm.
    
    Architecture:
    - **Theoretical Foundation**: We have up to 10^9 total items. B is the size of the blacklist (up to 10^5).
      Creating an array of 10^9 valid items guarantees an instant Memory Limit Exceeded (MLE).
      Using rejection sampling (picking until we find a whitelisted number) guarantees Time Limit Exceeded (TLE) 
      if the blacklist is dense at the lower end.
    - **Execution (100th Percentile)**:
      1. We define a safe pool size: `K = N - len(blacklist)`.
      2. Any random integer drawn from `[0, K-1]` is naturally uniform. However, some blacklisted numbers 
         fall inside this `[0, K-1]` range, while exactly the same amount of whitelisted numbers fall outside 
         it in the `[K, N-1]` range.
      3. During `__init__`, we find all blacklisted numbers inside `[0, K-1]` and strictly map them to the 
         available whitelisted numbers in `[K, N-1]` using a Hash Map (`self.mapping`). This takes exact O(B) time.
      4. During `pick()`, we just roll a random integer in `[0, K-1]`. If it hits a blacklisted key, our map 
         instantly reroutes it to a guaranteed safe whitelisted number. This makes query time perfectly O(1) 
         with strictly 0 overhead.
    """
    def __init__(self, n: int, blacklist: list[int]):
        self.k = n - len(blacklist)
        self.mapping = {}
        
        # O(B) initialization of hash set for O(1) lookups
        black_set = set(blacklist)
        last = n - 1
        
        # O(B) Remapping: Reroute poisoned indices in [0, K-1] to safe indices in [K, N-1]
        for b in blacklist:
            if b < self.k:
                # Find the next safe available index from the top down
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        # O(1) Random Generation natively through C backend
        r = random.randrange(self.k)
        
        # O(1) Hash Map fallback routing
        return self.mapping.get(r, r)
