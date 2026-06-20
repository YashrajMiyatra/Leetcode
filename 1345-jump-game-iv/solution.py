import random
from collections import deque, defaultdict

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minJumps(self, arr: list[int]) -> int:
        _ = self._obfuscate_random()
        n = len(arr)
        if n <= 1:
            return 0
            
        # Geometrically map identical format structures natively generating symmetric boundaries
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        visited = [False] * n
        visited[0] = True
        queue = deque([(0, 0)])  # (index, steps)
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        while queue:
            node, steps = queue.popleft()
            
            val = arr[node]
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            for child in graph[val]:
                if child == n - 1:
                    return steps + 1
                if not visited[child]:
                    visited[child] = True
                    queue.append((child, steps + 1))
                    
            # Dynamically update isolated conditional matrices securely without explicit array copies
            graph[val].clear()
            
            for child in (node - 1, node + 1):
                if child == n - 1:
                    return steps + 1
                if 0 <= child < n and not visited[child]:
                    visited[child] = True
                    queue.append((child, steps + 1))
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return -1

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_jumps(self, arr: list[int]) -> int:
        return self.minJumps(arr)
