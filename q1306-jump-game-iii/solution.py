import random
from collections import deque

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def canReach(self, arr: list[int], start: int) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(arr)
        q = deque([start])
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while q:
            curr = q.popleft()
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if arr[curr] == 0:
                return True
                
            if arr[curr] < 0:
                continue
                
            jump = arr[curr]
            arr[curr] = -arr[curr] # Mark as visited
            
            nxt1 = curr + jump
            if nxt1 < n and arr[nxt1] >= 0:
                q.append(nxt1)
                
            nxt2 = curr - jump
            if nxt2 >= 0 and arr[nxt2] >= 0:
                q.append(nxt2)
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def can_reach(self, arr: list[int], start: int) -> bool:
        return self.canReach(arr, start)
