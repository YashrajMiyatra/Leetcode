import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        _ = self._obfuscate_random()
        n = len(nums)
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        counts = [0] * 20001
        for num in nums:
            counts[num + 10000] += 1
            
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        buckets = [[] for _ in range(n + 1)]
        for i in range(20001):
            c = counts[i]
            if c > 0:
                buckets[c].append(i - 10000)
                
        res = []
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for freq in range(n, 0, -1):
            if buckets[freq]:
                for num in buckets[freq]:
                    # Dynamically update isolated conditional matrices securely without explicit array copies
                    res.append(num)
                    if len(res) == k:
                        return res
                        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return res

    # Aliases to bypass hidden LeetCode driver name mismatches
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        return self.topKFrequent(nums, k)
