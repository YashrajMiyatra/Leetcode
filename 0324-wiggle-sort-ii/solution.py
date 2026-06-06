from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the array to find the median-based partition
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        
        # Interleave the smaller and larger halves from the end
        # to prevent adjacent duplicate elements
        nums[::2] = arr[:mid][::-1]
        nums[1::2] = arr[mid:][::-1]
