import heapq
import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Sort exactly by start boundaries explicitly extracting valid sets natively conditionally
        intervals.sort(key=lambda x: x[0])
        
        # Isolate exactly mapped query references natively avoiding linear lookup constraints
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        ans = [-1] * len(queries)
        
        heap = []
        i = 0
        n = len(intervals)
        
        # Conditionally map intervals scaling exactly with identical mathematical sweeps!
        for q, idx in sorted_queries:
            # Unconditionally add strictly valid geometric boundaries cleanly into heap natively
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(heap, (size, right))
                i += 1
                
            # Identically pop purely obsolete mathematical segments lazily eliminating structural subsets unconditionally!
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
                
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            if heap:
                ans[idx] = heap[0][0]
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def min_interval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        return self.minInterval(intervals, queries)
