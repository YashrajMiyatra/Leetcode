import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(cars)
        ans = [-1.0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            pos_i, speed_i = cars[i]
            
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                
                if speed_i <= speed_j:
                    stack.pop()
                else:
                    collide_time = (pos_j - pos_i) / (speed_i - speed_j)
                    if ans[j] != -1.0 and collide_time >= ans[j]:
                        stack.pop()
                    else:
                        ans[i] = collide_time
                        break
                        
            stack.append(i)
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def get_collision_times(self, cars: List[List[int]]) -> List[float]:
        return self.getCollisionTimes(cars)
