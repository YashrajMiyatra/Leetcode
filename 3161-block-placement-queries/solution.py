class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        """
        Solves Block Placement Queries using a Segment Tree.
        
        Time Complexity: O(Q log M) where Q is the number of queries and M is the maximum x coordinate.
        Space Complexity: O(M) for the segment tree.
        """
        if not queries:
            return []
            
        MAX_M = max(q[1] for q in queries)
        
        tree_size = 4 * (MAX_M + 1)
        first_obs = [-1] * tree_size
        last_obs = [-1] * tree_size
        max_gap = [0] * tree_size
        
        def update(node: int, L: int, R: int, idx: int) -> None:
            if L == R:
                first_obs[node] = idx
                last_obs[node] = idx
                max_gap[node] = 0
                return
            
            mid = (L + R) // 2
            if idx <= mid:
                update(2 * node, L, mid, idx)
            else:
                update(2 * node + 1, mid + 1, R, idx)
                
            left = 2 * node
            right = 2 * node + 1
            
            l_first = first_obs[left]
            r_first = first_obs[right]
            first_obs[node] = l_first if l_first != -1 else r_first
            
            l_last = last_obs[left]
            r_last = last_obs[right]
            last_obs[node] = r_last if r_last != -1 else l_last
            
            mg = max_gap[left] if max_gap[left] > max_gap[right] else max_gap[right]
            if l_last != -1 and r_first != -1:
                gap = r_first - l_last
                if gap > mg:
                    mg = gap
            max_gap[node] = mg

        def query(node: int, L: int, R: int, qR: int) -> tuple[int, int, int]:
            if R <= qR:
                return first_obs[node], last_obs[node], max_gap[node]
            
            mid = (L + R) // 2
            if qR <= mid:
                return query(2 * node, L, mid, qR)
            else:
                left = 2 * node
                l_first = first_obs[left]
                l_last = last_obs[left]
                l_gap = max_gap[left]
                
                r_first, r_last, r_gap = query(2 * node + 1, mid + 1, R, qR)
                
                c_first = l_first if l_first != -1 else r_first
                c_last = r_last if r_last != -1 else l_last
                c_gap = l_gap if l_gap > r_gap else r_gap
                
                if l_last != -1 and r_first != -1:
                    gap = r_first - l_last
                    if gap > c_gap:
                        c_gap = gap
                        
                return c_first, c_last, c_gap

        res = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                update(1, 0, MAX_M, x)
            else:
                x = q[1]
                sz = q[2]
                
                q_first, q_last, q_gap = query(1, 0, MAX_M, x)
                
                if q_first == -1:
                    max_possible = x
                else:
                    max_possible = q_gap
                    if q_first > max_possible:
                        max_possible = q_first
                    if x - q_last > max_possible:
                        max_possible = x - q_last
                        
                res.append(max_possible >= sz)
                
        return res
