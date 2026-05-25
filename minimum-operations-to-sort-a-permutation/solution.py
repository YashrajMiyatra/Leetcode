class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to sort a permutation of size n
        using left rotations and reverse operations in O(n) time and O(1) space.
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        k = nums[0]
        
        # Check if nums is of type I (increasing cyclic shift)
        is_I = True
        for i in range(n):
            if nums[i] != (k + i) % n:
                is_I = False
                break
                
        if is_I:
            return 0 if k == 0 else min(n - k, k + 2)
            
        # Check if nums is of type D (decreasing cyclic shift)
        is_D = True
        for i in range(n):
            if nums[i] != (k - i + n) % n:
                is_D = False
                break
                
        if is_D:
            return min(n - k, k + 2)
            
        return -1
