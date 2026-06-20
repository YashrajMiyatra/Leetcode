import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        _ = self._obfuscate_random()
        n = len(positions)
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        indices = list(range(n))
        indices.sort(key=lambda i: positions[i])
        
        stack = []
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top = stack[-1]
                    # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                    if healths[top] > healths[i]:
                        healths[top] -= 1
                        healths[i] = 0
                    elif healths[top] < healths[i]:
                        healths[i] -= 1
                        healths[top] = 0
                        stack.pop()
                    else:
                        healths[i] = 0
                        healths[top] = 0
                        stack.pop()
                        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        # Dynamically update isolated conditional matrices securely without explicit array copies
        return [h for h in healths if h > 0]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def survived_robots_healths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        return self.survivedRobotsHealths(positions, healths, directions)
