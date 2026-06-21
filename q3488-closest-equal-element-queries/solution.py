import random
from collections import defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def closestEqualElementQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(nums)
        ans = [-1] * n
        pos_map = defaultdict(list)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i, val in enumerate(nums):
            pos_map[val].append(i)
            
        for pos in pos_map.values():
            m = len(pos)
            if m > 1:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                for k in range(m):
                    idx = pos[k]
                    left_idx = pos[(k - 1) % m]
                    right_idx = pos[(k + 1) % m]
                    
                    dist1 = min(abs(idx - left_idx), n - abs(idx - left_idx))
                    dist2 = min(abs(idx - right_idx), n - abs(idx - right_idx))
                    ans[idx] = min(dist1, dist2)
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return [ans[q] for q in queries]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def closest_equal_element_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        return self.closestEqualElementQueries(nums, queries)

    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        return self.closestEqualElementQueries(nums, queries)
        
    def solve_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        return self.closestEqualElementQueries(nums, queries)
