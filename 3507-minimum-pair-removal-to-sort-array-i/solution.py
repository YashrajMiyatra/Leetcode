class Solution:
    """
    Hyper-Optimized Single-Pass C-Level Array Simulation.
    
    Architecture:
    - **Theoretical Foundation**: The problem requires identifying if an array is sorted, and if not, finding 
      the pair with the absolute minimum sum to collapse. A naive approach loops the array twice: once to check 
      if it's sorted, and a second time to find the minimum pair.
    - **Execution (0ms Target)**:
      1. **Unified Single-Pass Inspection**: We merge the `is_sorted` check and the `min_sum` search into 
         a single, highly localized flat loop. We evaluate both conditions simultaneously per adjacent pair.
      2. **Zero-Allocation Mutations**: A standard slice replacement (`nums[i:i+2] = [min_s]`) implicitly allocates 
         a new single-element Python list object before triggering C's memmove. To strip this overhead, we use 
         `nums[min_i] = min_s` followed by `nums.pop(min_i + 1)`. This alters the values purely in-place and triggers 
         the pointer shift (`pop`) with zero dynamic object creation.
      3. **Variable Caching**: Length lookups are cached to avoid calling `len()` repeatedly inside the loop boundaries.
    """
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ops = 0
        while True:
            is_sorted = True
            min_s = float('inf')
            min_i = -1
            
            # Cache length to strip boundary check overhead
            n = len(nums)
            for i in range(n - 1):
                a = nums[i]
                b = nums[i+1]
                
                # Check sort invariant
                if a > b:
                    is_sorted = False
                
                # Check minimum sum pair
                s = a + b
                if s < min_s:
                    min_s = s
                    min_i = i
                    
            if is_sorted:
                return ops
                
            # Zero-allocation in-place mutation and pop (C-level pointer memmove)
            nums[min_i] = min_s
            nums.pop(min_i + 1)
            
            ops += 1
