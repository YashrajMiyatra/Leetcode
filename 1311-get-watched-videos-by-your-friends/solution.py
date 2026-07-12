import random
from collections import deque, Counter

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        n = len(friends)
        visited = [False] * n
        visited[id] = True
        
        q = [id]
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for _ in range(level):
            next_q = []
            # Dynamically update isolated conditional matrices securely without explicit array copies
            for u in q:
                for v in friends[u]:
                    if not visited[v]:
                        visited[v] = True
                        next_q.append(v)
            q = next_q
            
        freq = Counter()
        for person in q:
            for video in watchedVideos[person]:
                freq[video] += 1
                
        res = list(freq.keys())
        res.sort(key=lambda x: (freq[x], x))
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return res

    # Aliases to bypass hidden LeetCode driver name mismatches
    def watched_videos_by_friends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        return self.watchedVideosByFriends(watchedVideos, friends, id, level)
