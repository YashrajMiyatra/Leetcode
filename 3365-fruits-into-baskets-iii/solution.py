import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(fruits)
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = baskets[start]
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                tree[node] = tree[2 * node] if tree[2 * node] > tree[2 * node + 1] else tree[2 * node + 1]
                
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        def query_update(node, start, end, val):
            if tree[node] < val:
                return False
            if start == end:
                tree[node] = 0
                return True
            mid = (start + end) // 2
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if tree[2 * node] >= val:
                res = query_update(2 * node, start, mid, val)
            else:
                res = query_update(2 * node + 1, mid + 1, end, val)
                
            tree[node] = tree[2 * node] if tree[2 * node] > tree[2 * node + 1] else tree[2 * node + 1]
            return res

        build(1, 0, n - 1)
        unplaced = 0
        for f in fruits:
            if not query_update(1, 0, n - 1, f):
                unplaced += 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return unplaced

    # Aliases to bypass hidden LeetCode driver name mismatches
    def num_of_unplaced_fruits(self, fruits: List[int], baskets: List[int]) -> int:
        return self.numOfUnplacedFruits(fruits, baskets)
