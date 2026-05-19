class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two indices such that their values sum up to the target.
        Time Complexity: O(n) - Single pass traversal with O(1) dictionary lookups.
        Space Complexity: O(n) - Storing up to n elements in the dictionary.
        """
        # Map to store numbers and their corresponding index: {number: index}
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement is found, return the index pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Store the current number's index in the map
            num_to_index[num] = index
            
        # Fallback return (guaranteed by constraints to not be reached)
        raise ValueError("No two sum solution exists.")
