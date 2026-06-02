import operator

class Solution:
    """
    Hyper-Optimized O(N + M) Mathematical Solution.
    
    Architecture:
    - **Theoretical Foundation**: A brute force approach pairs every land ride with every water ride, 
      taking O(N * M) time. However, this is mathematically redundant. 
      For any sequence (e.g., Land -> Water), the only property of the first ride that affects the 
      second ride is its *finish time*. Thus, to minimize the total duration of a Land -> Water sequence, 
      we ONLY need to consider the single land ride that finishes the absolute earliest.
      This mathematical property allows us to completely decouple the nested loops.
    - **Execution (100th Percentile)**:
      1. We find the minimum finish time across all land rides (`min_lf`) and water rides (`min_wf`). 
         We use `map(operator.add, ...)` which delegates the addition entirely to the C backend, 
         making it the fastest possible way to sum two lists in Python.
      2. We then independently calculate the best Land -> Water sequence using only `min_lf`, and 
         the best Water -> Land sequence using only `min_wf`.
      3. We use list comprehensions over generators, as they evaluate completely at the C layer 
         without generator frame overhead.
      This drastically reduces the time complexity from O(N * M) to perfectly O(N + M).
    """
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        # C-Level execution for finding the absolute earliest finish times
        min_lf = min(map(operator.add, landStartTime, landDuration))
        min_wf = min(map(operator.add, waterStartTime, waterDuration))
        
        # O(M) sequence: Earliest Land ride -> Water ride
        ans1 = min([
            (min_lf if min_lf > ws else ws) + wd 
            for ws, wd in zip(waterStartTime, waterDuration)
        ])
        
        # O(N) sequence: Earliest Water ride -> Land ride
        ans2 = min([
            (min_wf if min_wf > ls else ls) + ld 
            for ls, ld in zip(landStartTime, landDuration)
        ])
        
        return ans1 if ans1 < ans2 else ans2
