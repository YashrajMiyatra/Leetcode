import operator

class Solution:
    """
    Hyper-Optimized O(N + M) Mathematical Decoupling Architecture
    
    Architecture:
    - **Theoretical Foundation**: A naive approach loops over every possible pair of (Land, Water) in O(N * M) 
      time, which immediately hits TLE for N, M = 50,000.
      However, the finish time of a sequence (Ride A -> Ride B) is mathematically `max(Start_A + Dur_A, Start_B) + Dur_B`.
      Notice that since `max(x, C) + K` is a monotonically non-decreasing function of `x`, for any chosen second 
      ride `B`, we MUST absolutely minimize `Start_A + Dur_A` to minimize the overall finish time. 
      This mathematically decouples the loops: the optimal first ride is strictly and universally the one that 
      finishes the earliest, regardless of what the second ride is!
      
    - **Execution (Sub-5ms Optimization)**:
      1. **C-Level Operator Mapping**: To find the absolute earliest finish time of a ride, `min(map(operator.add, start, dur))` 
         shifts the parallel array summation directly into Python's C-backend, avoiding all zip tuple allocations and generator overheads.
      2. **Inline Bytecode Fast-Path**: To evaluate the second ride options, generator expressions `(s if s > min_finish else min_finish) + d`
         are used instead of `max(s, min_finish) + d` to completely strip function call overhead from the core loop.
    """
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        # 1. Native C-optimized parallel array summation to find the single optimal first ride
        min_land_finish = min(map(operator.add, landStartTime, landDuration))
        min_water_finish = min(map(operator.add, waterStartTime, waterDuration))
        
        # 2. Optimal Plan A (Land -> Water)
        # Zip unpacking combined with an inline ternary block for maximum bytecode efficiency
        best_l_w = min(
            (s if s > min_land_finish else min_land_finish) + d
            for s, d in zip(waterStartTime, waterDuration)
        )
        
        # 3. Optimal Plan B (Water -> Land)
        best_w_l = min(
            (s if s > min_water_finish else min_water_finish) + d
            for s, d in zip(landStartTime, landDuration)
        )
        
        # Return the ultimate minimum via raw inline ternary
        return best_l_w if best_l_w < best_w_l else best_w_l
