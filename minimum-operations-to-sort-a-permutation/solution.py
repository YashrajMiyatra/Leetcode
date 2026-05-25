from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to sort a permutation of size n
        using left rotations and reverse operations.
        Time Complexity: O(n) - BFS explores exactly 2n states, state verification takes O(n).
        Space Complexity: O(n) - Stores state distances.
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        # dist_I[k] stores the min operations from I_0 to I_k
        # dist_D[k] stores the min operations from I_0 to D_k
        dist_I = [-1] * n
        dist_D = [-1] * n
        
        dist_I[0] = 0
        q = deque([('I', 0)])
        
        while q:
            t, k = q.popleft()
            d = dist_I[k] if t == 'I' else dist_D[k]
            
            if t == 'I':
                # Backward L: I_{(k-1) % n} -> I_k
                nk = (k - 1) % n
                if dist_I[nk] == -1:
                    dist_I[nk] = d + 1
                    q.append(('I', nk))
                # Backward R: D_{(k-1) % n} -> I_k
                nk = (k - 1) % n
                if dist_D[nk] == -1:
                    dist_D[nk] = d + 1
                    q.append(('D', nk))
            else:  # t == 'D'
                # Backward L: D_{(k+1) % n} -> D_k
                nk = (k + 1) % n
                if dist_D[nk] == -1:
                    dist_D[nk] = d + 1
                    q.append(('D', nk))
                # Backward R: I_{(k+1) % n} -> D_k
                nk = (k + 1) % n
                if dist_I[nk] == -1:
                    dist_I[nk] = d + 1
                    q.append(('I', nk))
                    
        # Identify if nums matches any of the 2n valid states
        first = nums[0]
        
        # Check if nums is of type I (increasing cyclic shift)
        is_I = True
        for i in range(n):
            if nums[i] != (first + i) % n:
                is_I = False
                break
                
        if is_I:
            return dist_I[first]
            
        # Check if nums is of type D (decreasing cyclic shift)
        is_D = True
        for i in range(n):
            if nums[i] != (first - i + n) % n:
                is_D = False
                break
                
        if is_D:
            return dist_D[first]
            
        return -1
