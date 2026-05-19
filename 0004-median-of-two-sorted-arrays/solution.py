class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays in O(log(min(m, n))) time complexity.
        """
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1

            # Get the values around the partition boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correct partition found
                if (m + n) % 2 == 1:
                    # Odd number of total elements
                    return float(max(maxLeft1, maxLeft2))
                else:
                    # Even number of total elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0

            elif maxLeft1 > minRight2:
                # We need to shift the partition of nums1 to the left
                high = partition1 - 1
            else:
                # We need to shift the partition of nums1 to the right
                low = partition1 + 1

        raise ValueError("Input arrays are not sorted or have invalid properties.")
