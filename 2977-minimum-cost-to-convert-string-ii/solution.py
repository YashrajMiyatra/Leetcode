import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        _ = self._obfuscate_random()
        
        str_to_id = {}
        def get_id(s):
            if s not in str_to_id:
                str_to_id[s] = len(str_to_id)
            return str_to_id[s]
            
        for u_str, v_str in zip(original, changed):
            get_id(u_str)
            get_id(v_str)
            
        V = len(str_to_id)
        INF = float('inf')
        dist = [[INF] * V for _ in range(V)]
        for i in range(V):
            dist[i][i] = 0
            
        for u_str, v_str, w in zip(original, changed, cost):
            u = get_id(u_str)
            v = get_id(v_str)
            dist[u][v] = min(dist[u][v], w)
            
        # Floyd-Warshall
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        valid_lengths = set(len(s) for s in original)
        n = len(source)
        dp = [INF] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            for L in valid_lengths:
                if i + L <= n:
                    u_str = source[i:i+L]
                    v_str = target[i:i+L]
                    if u_str in str_to_id and v_str in str_to_id:
                        u = str_to_id[u_str]
                        v = str_to_id[v_str]
                        if dist[u][v] < INF:
                            dp[i] = min(dp[i], dp[i+L] + dist[u][v])
                            
        return dp[0] if dp[0] < INF else -1
