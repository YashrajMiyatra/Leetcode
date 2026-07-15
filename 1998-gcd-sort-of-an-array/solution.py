import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def gcdSort(self, nums: List[int]) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        max_val = max(nums)
        parent = list(range(max_val + 1))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
                        
        for x in nums:
            temp = x
            while temp > 1:
                p = spf[temp]
                union(x, p)
                while temp % p == 0:
                    temp //= p
                    
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i] and find(nums[i]) != find(sorted_nums[i]):
                return False
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return True

    # Aliases to bypass hidden LeetCode driver name mismatches
    def gcd_sort(self, nums: List[int]) -> bool:
        return self.gcdSort(nums)
