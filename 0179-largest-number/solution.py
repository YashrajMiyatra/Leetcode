from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings
        nums_str = [str(x) for x in nums]
        
        # Custom comparator: x comes before y if x+y > y+x
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0
            
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted list
        result = "".join(nums_str)
        
        # Handle the edge case of all zeros (e.g. [0, 0] -> "0")
        return "0" if result[0] == "0" else result
