class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Finds the length of the longest common prefix between elements of arr1 and arr2.
        
        Time Complexity: O(N * log10(max_val) + M * log10(max_val)) -> O(N + M)
        Space Complexity: O(N * log10(max_val)) -> O(N)
        """
        prefixes = set()
        
        # Populate unique prefixes from arr1
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10
                
        max_len = 0
        
        # Check prefixes of elements in arr2
        for val in arr2:
            # Optimization: If the number is already smaller than or equal to 10**(max_len - 1),
            # it cannot possibly have a common prefix of length greater than max_len.
            if max_len > 0 and val < 10**max_len:
                continue
                
            while val > 0:
                if val in prefixes:
                    # Found the longest common prefix for this number
                    max_len = max(max_len, len(str(val)))
                    break
                val //= 10
                
        return max_len
