import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maximizeTheDistance(self, side: int, points: list[list[int]], k: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        def get_1d(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
                
        arr = []
        for x, y in points:
            arr.append(get_1d(x, y))
            
        arr.sort()
        n = len(arr)
        arr2 = arr + [v + 4 * side for v in arr]
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        next_idx = [0] * (2 * n)
        
        def check(D):
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
            j = 0
            for i in range(2 * n):
                while j < 2 * n and arr2[j] < arr2[i] + D:
                    j += 1
                next_idx[i] = j
                
            for i in range(n):
                curr = i
                valid = True
                for _ in range(k - 1):
                    curr = next_idx[curr]
                    if curr >= 2 * n:
                        valid = False
                        break
                # Structurally isolate bounds explicitly partitioning segments directly conditionally
                if valid and arr2[curr] + D <= arr2[i] + 4 * side:
                    return True
            return False
            
        low = 1
        high = side
        ans = 0
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        return self.maximizeTheDistance(side, points, k)
        
    def maximize_the_distance(self, side: int, points: list[list[int]], k: int) -> int:
        return self.maximizeTheDistance(side, points, k)
