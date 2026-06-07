from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        # Helper to compute the largest rectangle area in a histogram
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_a = 0
            # Append 0 to flush the stack at the end
            heights.append(0)
            
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    # If stack is empty, width extends to the beginning of the histogram
                    width = i if not stack else i - stack[-1] - 1
                    area = height * width
                    if area > max_a:
                        max_a = area
                stack.append(i)
                
            heights.pop() # Restore heights
            return max_a

        for row in matrix:
            # Update heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find the max rectangle area for the current histogram of heights
            row_area = largestRectangleArea(heights)
            if row_area > max_area:
                max_area = row_area
                
        return max_area
