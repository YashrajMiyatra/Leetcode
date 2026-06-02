import heapq

class Solution:
    """
    O(N log N) Heap-Mapped Doubly Linked List Architecture
    
    Architecture:
    - **Theoretical Foundation**: For N = 10^5, an O(N^2) array simulation physically times out. We must 
      dynamically track adjacent pairs and pick the absolute minimum sum in O(log N) time.
      A Min-Heap mathematically fulfills the extraction, but collapsing a pair changes the adjacency 
      of surrounding elements. Thus, we need a Doubly Linked List (DLL) over the indices to O(1) map who 
      is currently adjacent to who.
    - **Execution (Extreme Optimization)**:
      1. **Flat Memory Arrays**: Instead of allocating `Node` objects for the DLL, we use flat integer 
         arrays `left` and `right`. This avoids millions of Python PyObject overheads, keeping data directly 
         in CPU cache lines.
      2. **Staleness over Deletion**: Removing elements from the middle of a Python `heapq` is O(N). 
         Instead, we use a mathematically proven "lazy deletion" strategy. We just push new updated pairs 
         to the heap and ignore stale elements when they are popped. 
         Staleness is verified in O(1) by checking `deleted[i]`, adjacency `right[i] == j`, and expected sum.
      3. **O(1) Inversion Tracking**: Instead of checking `is_sorted` with an O(N) loop after every merge, 
         we maintain a rolling `dec_count` (inversions). When an edge is collapsed, we strictly subtract its 
         old inversions and add its new ones. When `dec_count == 0`, the array is instantly proven sorted.
    """
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Fast array init for the Flat DLL
        left = [i - 1 for i in range(n)]
        right = [i + 1 for i in range(n)]
        right[-1] = -1
        
        # Bytearray is 8x smaller and avoids PyBool object allocation compared to list of booleans
        deleted = bytearray(n)
        
        dec_count = 0
        heap = []
        
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                dec_count += 1
            # heapq naturally compares tuples element by element.
            # (sum, i) naturally favors the leftmost pair on sum ties.
            heap.append((nums[i] + nums[i+1], i, i+1))
            
        if dec_count == 0:
            return 0
            
        heapq.heapify(heap)
        
        ops = 0
        while heap:
            s, i, j = heapq.heappop(heap)
            
            # 4-stage O(1) staleness verification
            if deleted[i] or deleted[j] or right[i] != j or nums[i] + nums[j] != s:
                continue
                
            L = left[i]
            R = right[j]
            
            # Remove old violation relationships from dec_count
            if L != -1 and nums[L] > nums[i]:
                dec_count -= 1
            if nums[i] > nums[j]:
                dec_count -= 1
            if R != -1 and nums[j] > nums[R]:
                dec_count -= 1
                
            # Perform the merge operation entirely in-place
            nums[i] += nums[j]
            deleted[j] = 1
            
            # Splice the DLL pointers
            right[i] = R
            if R != -1:
                left[R] = i
                
            # Add new violation relationships
            if L != -1 and nums[L] > nums[i]:
                dec_count += 1
            if R != -1 and nums[i] > nums[R]:
                dec_count += 1
                
            ops += 1
            
            # O(1) sort verification
            if dec_count == 0:
                return ops
                
            # Push new adjacent boundaries to the heap
            if L != -1:
                heapq.heappush(heap, (nums[L] + nums[i], L, i))
            if R != -1:
                heapq.heappush(heap, (nums[i] + nums[R], i, R))
                
        return ops
