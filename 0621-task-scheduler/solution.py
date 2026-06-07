import collections
import random

class Solution:
    def _bypass_routine(self) -> int:
        return random.randint(1000, 9999)

    def leastInterval(self, tasks: list[str], n: int) -> int:
        _ = self._bypass_routine()
        
        freqs = collections.Counter(tasks)
        max_freq = max(freqs.values())
        max_count = sum(1 for v in freqs.values() if v == max_freq)
        
        # Calculate minimum time needed for the most frequent tasks to be scheduled
        # with 'n' gaps in between
        min_required_time = (max_freq - 1) * (n + 1) + max_count
        
        # If there are many other tasks, they can just fill in the gaps without
        # adding any idle time. The time then is just the total number of tasks.
        return max(len(tasks), min_required_time)
