class Solution:
    def minElement(self, nums: list[int]) -> int:
        """
        Calculates the sum of digits for each number and returns the minimum sum.
        
        Time Complexity: O(n * log10(M)) where n is the number of elements and M is the maximum element.
        Space Complexity: O(1)
        """
        ans = float('inf')
        for num in nums:
            curr_sum = 0
            while num > 0:
                curr_sum += num % 10
                num //= 10
            if curr_sum < ans:
                ans = curr_sum
        return ans
