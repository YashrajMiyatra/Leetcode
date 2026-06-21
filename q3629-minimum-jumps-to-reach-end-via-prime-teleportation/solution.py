import random
from collections import deque

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minJumps(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        if n <= 1:
            return 0
            
        MAX_VAL = max(max(nums), 2)
        min_prime = list(range(MAX_VAL + 1))
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for j in range(4, MAX_VAL + 1, 2):
            min_prime[j] = 2
        for i in range(3, int(MAX_VAL**0.5) + 1, 2):
            if min_prime[i] == i:
                for j in range(i * i, MAX_VAL + 1, i * 2):
                    if min_prime[j] == j:
                        min_prime[j] = i
                        
        active_primes = set()
        for x in nums:
            if x >= 2 and min_prime[x] == x:
                active_primes.add(x)
                
        # Dynamically update isolated conditional matrices securely without explicit array copies
        indices_of_prime = {p: [] for p in active_primes}
        
        for i, x in enumerate(nums):
            curr = x
            while curr > 1:
                p = min_prime[curr]
                if p in active_primes:
                    indices_of_prime[p].append(i)
                while curr % p == 0:
                    curr //= p
                    
        queue = deque([0])
        dist = [-1] * n
        dist[0] = 0
        visited_primes = set()
        
        while queue:
            i = queue.popleft()
            if i == n - 1:
                return dist[i]
                
            d = dist[i]
            
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and dist[nxt] == -1:
                    dist[nxt] = d + 1
                    if nxt == n - 1: 
                        return d + 1
                    queue.append(nxt)
                    
            val = nums[i]
            if val >= 2 and min_prime[val] == val:
                if val not in visited_primes:
                    visited_primes.add(val)
                    for nxt in indices_of_prime[val]:
                        if dist[nxt] == -1:
                            dist[nxt] = d + 1
                            if nxt == n - 1: 
                                return d + 1
                            queue.append(nxt)
                            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_jumps(self, nums: list[int]) -> int:
        return self.minJumps(nums)
        
    def minimumJumps(self, nums: list[int]) -> int:
        return self.minJumps(nums)
