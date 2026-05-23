class Solution:
    def check(self, nums: list[int]) -> bool:
        """
        Checks if the array was originally sorted in non-decreasing order, then rotated.
        Time Complexity: O(n) - Single pass over the array of size n.
        Space Complexity: O(1) - Constant extra space.
        """
        n = len(nums)
        inflection_points = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                inflection_points += 1
                
        return inflection_points <= 1
