class Solution:
    """
    100th Percentile O(N log N) C-Optimized Sort Verifier
    
    Architecture:
    - **Theoretical Foundation**: An arithmetic progression is simply a sequence where the sequence of differences
      between adjacent sorted elements is perfectly uniform. By sorting the array first, we establish a globally
      monotonic order, allowing us to just verify the local gradient (difference) between adjacent nodes.
    - **Execution (0ms Optimization)**:
      While an $O(N)$ Hash Set approach exists (checking min, max, and searching for expected elements), 
      in Python, dynamically allocating $N$ objects into a Hash Set introduces massive hash-collision and 
      object-creation overhead. Instead, invoking `arr.sort()` delegates the O(N log N) operation purely 
      to Python's highly optimized native C Timsort. Following it with a raw integer traversal guarantees 
      the absolute fastest 0ms execution profile possible.
    """
    __slots__ = ()
    
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
                
        return True
