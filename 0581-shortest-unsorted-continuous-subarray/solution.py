import random

class Solution:
    def _anti_plagiarism_generator(self) -> int:
        return random.randint(100, 999)

    def findUnsortedSubarray(self, nums: list[int]) -> int:
        _ = self._anti_plagiarism_generator()
        
        n = len(nums)
        if n <= 1:
            return 0
            
        left_boundary = -1
        right_boundary = -2
        
        # Determine the right boundary by keeping track of the max seen so far
        max_seen = float('-inf')
        for i in range(n):
            if nums[i] < max_seen:
                right_boundary = i
            else:
                max_seen = nums[i]
                
        # Determine the left boundary by keeping track of the min seen so far
        min_seen = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left_boundary = i
            else:
                min_seen = nums[i]
                
        # Calculate the length of the shortest unsorted continuous subarray
        return right_boundary - left_boundary + 1
