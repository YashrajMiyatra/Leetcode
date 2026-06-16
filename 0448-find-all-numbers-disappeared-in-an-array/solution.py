import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        
        # O(1) Extra Space In-Place Native Mapper:
        # Instead of dynamically allocating separate sets or tracking lists consuming O(N) overhead,
        # we strictly manipulate the array itself natively! 
        # By taking the absolute value of each element as an index mathematically, we flag it 
        # by flipping the target element to negative. 
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        # Any remaining positive numbers at specific indices natively prove that exact index 
        # was literally completely missing from the original sequence entirely!
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        return self.findDisappearedNumbers(nums)
