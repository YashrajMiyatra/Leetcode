class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        """
        Limits occurrences of each distinct element in a sorted array nums to at most k.
        Time Complexity: O(n) - Single pass over the array of size n.
        Space Complexity: O(1) - Modifies the array in-place.
        """
        n = len(nums)
        if n == 0:
            return []
            
        write_index = 0
        for read_index in range(n):
            if write_index < k or nums[read_index] != nums[write_index - k]:
                nums[write_index] = nums[read_index]
                write_index += 1
                
        return nums[:write_index]
