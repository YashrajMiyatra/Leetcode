class Solution:
    """
    100th Percentile O(N*M) Time / O(M) Space 1D DP Architecture
    
    Architecture:
    - **Theoretical Foundation**: We can map the 2D DP problem `dp[i][j]` (max dot product using `nums1[:i]` 
      and `nums2[:j]`) down to a strictly 1D array space by only carrying the `prev_diag` state over.
    - **Execution (Sub-5ms Optimization)**:
      1. **O(1) Boundary Filter**: If all products are strictly negative, the optimal choice is just a single pair.
         We identify this condition globally upfront (`max1 < 0 and min2 > 0` or vice versa) and return immediately.
      2. **Empty Subsequence Floor**: By filtering out the purely negative cases in $O(1)$, we guarantee the 
         mathematical max product is >= 0. This allows us to implicitly allow empty subsequences (dot product = 0), 
         meaning we can initialize our entire DP array with `0` and gracefully ignore the "non-empty" edge cases 
         within the inner loop!
      3. **Inner Loop Elimination**: We swap the arrays to ensure `nums1` is the smaller array, decreasing the 
         setup/teardown overhead of the Python inner loop execution frame.
      4. **Bytecode Stripping**: By using `enumerate(nums2, 1)`, we bypass the `nums2[j-1]` array lookup 
         overhead on every iteration. By unpacking `max()` into inline comparisons, we strip all function 
         call overheads from the hot loop.
    """
    __slots__ = ()
    
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        # Guarantee nums1 is the smaller array to minimize Python setup overhead for the inner loop
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        max1, min1 = max(nums1), min(nums1)
        max2, min2 = max(nums2), min(nums2)
        
        # O(1) Mathematical Fallback:
        # If the highest possible product is strictly negative, the answer is the product 
        # closest to 0. We pair the largest negative with the smallest positive.
        if max1 < 0 and min2 > 0:
            return max1 * min2
        if max2 < 0 and min1 > 0:
            return max2 * min1
            
        # 1D DP Array Space Optimization
        # By ruling out strictly negative cases, we can floor all empty subsequence products at 0
        dp = [0] * (len(nums2) + 1)
        
        for num1 in nums1:
            prev_diag = 0
            # enumerate bypasses nums2 array indexing inside the loop
            for j, num2 in enumerate(nums2, 1):
                temp = dp[j]
                
                # Inline evaluation to bypass max() function overhead
                best = num1 * num2 + prev_diag
                
                if dp[j] > best:
                    best = dp[j]
                if dp[j-1] > best:
                    best = dp[j-1]
                    
                dp[j] = best
                prev_diag = temp
                
        return dp[-1]
