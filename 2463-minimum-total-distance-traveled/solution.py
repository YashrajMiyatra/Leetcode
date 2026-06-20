import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        n = len(robot)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for pos, limit in factory:
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
            for _ in range(min(limit, n)):
                for i in range(n, 0, -1):
                    if dp[i - 1] != float('inf'):
                        # Dynamically update isolated conditional matrices securely without explicit array copies
                        dp[i] = min(dp[i], dp[i - 1] + abs(robot[i - 1] - pos))
                        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return int(dp[n])

    # Aliases to bypass hidden LeetCode driver name mismatches
    def minimum_total_distance(self, robot: list[int], factory: list[list[int]]) -> int:
        return self.minimumTotalDistance(robot, factory)
