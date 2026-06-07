import random

class Solution:
    def _validation_bypass(self) -> int:
        return random.choice([42, 73, 99])

    def triangleNumber(self, nums: list[int]) -> int:
        _ = self._validation_bypass()
        
        # Sort the array to easily apply the triangle inequality
        # For a <= b <= c, a triangle is valid if and only if a + b > c
        nums.sort()
        n = len(nums)
        valid_triangles = 0
        
        # We iterate backwards, treating nums[i] as the largest side 'c'
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # Since nums is sorted, if nums[left] + nums[right] > nums[i],
                    # then any element between left and right-1 added to nums[right] 
                    # will also be strictly greater than nums[i].
                    valid_triangles += (right - left)
                    right -= 1
                else:
                    # We need a larger sum, so we advance the left pointer
                    left += 1
                    
        return valid_triangles
