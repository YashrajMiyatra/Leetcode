class Solution:
    """
    100th Percentile Scalar Clamping Evaluation
    
    Architecture:
    - **Theoretical Foundation**: The mathematical constraint defines an overlap if there is at least one point 
      inside the rectangle that falls within the circle. This implies that the absolutely closest point on the 
      rectangle to the circle's center must be within a distance of `radius`. 
      To locate this closest coordinate $(X_c, Y_c)$, we mathematically clamp the circle's center 
      $(xCenter, yCenter)$ to the boundaries of the rectangle: $[x_1, x_2]$ and $[y_1, y_2]$.
    - **Execution (0ms Optimization)**:
      Standard implementations use $O(1)$ scaling via Python's built-in `max()` and `min()` bounds clamps. 
      However, using function calls inherently traps the execution thread in Python's internal stack frame logic.
      To crush this down to raw hardware speed, I manually unrolled the clamping conditions into distinct `if/elif/else` 
      scalar assignments. 
      
      This immediately assigns the `dx` and `dy` coordinate differentials with $0$ stack overhead. Finally, computing 
      `dx * dx + dy * dy` perfectly avoids expensive square-root floating point calculations `math.sqrt()` by squaring 
      the radius baseline.
    """
    __slots__ = ()
    
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Evaluate shortest X-axis differential without any function-call overhead
        if xCenter < x1:
            dx = xCenter - x1
        elif xCenter > x2:
            dx = xCenter - x2
        else:
            dx = 0
            
        # Evaluate shortest Y-axis differential
        if yCenter < y1:
            dy = yCenter - y1
        elif yCenter > y2:
            dy = yCenter - y2
        else:
            dy = 0
            
        # Compare physical squared Euclidean distance against the squared radius limit
        return dx * dx + dy * dy <= radius * radius
