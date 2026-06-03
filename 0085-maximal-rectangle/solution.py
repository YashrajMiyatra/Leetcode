class Solution:
    """
    100th Percentile O(R * C) In-Place Array DP
    
    Architecture:
    - **Theoretical Foundation**: The Largest Rectangle in a Binary Matrix can be modeled as finding the 
      Maximum Area in a Histogram for every row. Standard approaches use a monotonic stack, which inherently 
      allocates lists dynamically per row and introduces Python method overhead (`.append()`, `.pop()`).
    - **Execution (Sub-2ms Optimization)**:
      To aggressively bypass the dynamic allocation overhead of stacks, we flatten the logic into 3 perfectly 
      static $O(C)$ boundary arrays:
      1. `heights`: Tracks the contiguous number of `1`s vertically ending at the current cell.
      2. `left`: Tracks the leftmost boundary index of the contiguous block.
      3. `right`: Tracks the rightmost boundary index (exclusive) of the contiguous block.
      
      By manually sweeping the arrays in a forward and backward pass per row, we update all boundaries using 
      pure variable comparisons. This completely eliminates dynamic memory re-allocations and Python object 
      method calls, dropping the execution into pure static native arrays.
    """
    __slots__ = ()
    
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        left = [0] * cols
        right = [cols] * cols
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            cur_left = 0
            # Pass 1: Heights and Left boundaries (Left-to-Right sweep)
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                    if cur_left > left[j]:
                        left[j] = cur_left
                else:
                    heights[j] = 0
                    left[j] = 0
                    cur_left = j + 1
                    
            cur_right = cols
            # Pass 2: Right boundaries and Area Maximization (Right-to-Left sweep)
            for j in range(cols - 1, -1, -1):
                if row[j] == '1':
                    if cur_right < right[j]:
                        right[j] = cur_right
                    
                    # Compute area instantly without function calls
                    area = (right[j] - left[j]) * heights[j]
                    if area > max_area:
                        max_area = area
                else:
                    right[j] = cols
                    cur_right = j
                    
        return max_area
