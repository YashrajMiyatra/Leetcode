from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Helper to check if nums can be split into <= k subarrays with max sum <= target
        def canSplit(target: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > target:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
            
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
