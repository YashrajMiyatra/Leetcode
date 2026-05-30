import heapq

class Twitter:
    """
    Hyper-optimized Twitter Feed.
    
    Architecture:
    - __slots__: Disables dynamic dictionary generation for absolute minimal memory footprint.
    - K-Way Merge: Employs a Min-Heap to execute a highly selective, partial multi-way 
      merge of chronologically sorted arrays. This strictly limits computational 
      complexity to O(10 * log F), where F is the number of followees, avoiding the 
      catastrophic O(T) scan overhead of a centralized global timeline array.
    """
    __slots__ = ['time', 'tweets', 'following']

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        tw = self.tweets.get(userId)
        if tw is None:
            tw = []
            self.tweets[userId] = tw
            
        # Time counts negatively downward so python's default min-heap inherently prioritizes newest tweets
        tw.append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        
        # O(1) Fetch user's own latest tweet
        tw = self.tweets.get(userId)
        if tw:
            idx = len(tw) - 1
            # Tuple structure: (negative_timestamp, tweetId, userId, index_in_user_array)
            heap.append((tw[idx][0], tw[idx][1], userId, idx))
            
        # O(F) Fetch each followee's latest tweet
        followees = self.following.get(userId)
        if followees:
            for u in followees:
                tw = self.tweets.get(u)
                if tw:
                    idx = len(tw) - 1
                    heap.append((tw[idx][0], tw[idx][1], u, idx))
                    
        # C-level Optimized Heap Generation O(F)
        heapq.heapify(heap)
        
        # O(10 * log F) greedy multi-way merge
        while heap and len(res) < 10:
            t, t_id, u, idx = heap[0]
            res.append(t_id)
            
            # Step backward in chronological history
            if idx > 0:
                nxt_idx = idx - 1
                nt, nt_id = self.tweets[u][nxt_idx]
                
                # heapreplace executes heappop + heappush internally in C, drastically outperforming sequential calls
                heapq.heapreplace(heap, (nt, nt_id, u, nxt_idx))
            else:
                heapq.heappop(heap)
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
            
        f = self.following.get(followerId)
        if f is None:
            f = set()
            self.following[followerId] = f
            
        f.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        f = self.following.get(followerId)
        if f:
            # discard drops an element in strict O(1) without throwing KeyErrors if not present
            f.discard(followeeId)
