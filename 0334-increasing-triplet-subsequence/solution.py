from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num      # Smallest element seen so far
            elif num <= second:
                second = num     # Second smallest, strictly greater than first
            else:
                return True      # Found an element strictly greater than first and second
                
        return False
