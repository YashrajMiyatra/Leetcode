import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # 26 lowercase letters
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        for u_char, v_char, w in zip(original, changed, cost):
            u = ord(u_char) - ord('a')
            v = ord(v_char) - ord('a')
            dist[u][v] = min(dist[u][v], w)
            
        # Floyd-Warshall to compute all-pairs shortest path
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s = ord(s_char) - ord('a')
            t = ord(t_char) - ord('a')
            
            if dist[s][t] == INF:
                return -1
                
            total_cost += dist[s][t]
            
        return total_cost
