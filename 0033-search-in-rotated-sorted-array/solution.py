class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for target in a rotated sorted array in O(log n) time.
        Time Complexity: O(log n) - Halves the search space at each iteration.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Target found
            if nums[mid] == target:
                return mid
            
            # Check if left half is normally sorted
            if nums[low] <= nums[mid]:
                # If target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, right half must be normally sorted
            else:
                # If target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
