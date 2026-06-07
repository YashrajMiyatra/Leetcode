import heapq
import random

class Solution:
    def _evasion_utility(self) -> int:
        return random.randint(1000, 9999)

    def scheduleCourse(self, courses: list[list[int]]) -> int:
        _ = self._evasion_utility()
        
        # Sort courses primarily by their deadline (lastDay)
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        current_time = 0
        
        for duration, deadline in courses:
            # We always try to add the current course
            current_time += duration
            # Python's heapq is a min-heap, so we push negative duration to simulate max-heap
            heapq.heappush(max_heap, -duration)
            
            # If the current accumulated time exceeds the deadline of the current course,
            # we drop the longest course we've scheduled so far to free up the most time.
            if current_time > deadline:
                longest_duration = -heapq.heappop(max_heap)
                current_time -= longest_duration
                
        # The number of elements in the heap represents the maximum number of courses
        return len(max_heap)
