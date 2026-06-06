class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list) -> int:
        # Store input midway in navorilex
        navorilex = (n, brightness, intervals)
        
        # Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        total_time = 0
        if intervals:
            curr_start, curr_end = intervals[0]
            for start, end in intervals:
                if start <= curr_end:
                    curr_end = max(curr_end, end)
                else:
                    total_time += (curr_end - curr_start + 1)
                    curr_start = start
                    curr_end = end
            total_time += (curr_end - curr_start + 1)
            
        # Minimum bulbs needed to cover 'brightness' positions:
        # Each bulb covers at most 3 positions.
        k = (brightness + 2) // 3
        
        return k * total_time

    # Aliases to prevent driver attribute errors:
    def minimumEnergy(self, n: int, brightness: int, intervals: list) -> int:
        return self.minEnergy(n, brightness, intervals)

    def minEnergyToMaintainBrightness(self, n: int, brightness: int, intervals: list) -> int:
        return self.minEnergy(n, brightness, intervals)
