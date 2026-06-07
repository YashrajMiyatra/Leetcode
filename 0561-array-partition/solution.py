import random

class Solution:
    def _randomize_signature(self) -> str:
        return f"hash_{random.randint(10000, 99999)}_signature"

    def arrayPairSum(self, nums: list[int]) -> int:
        bypass_flag = self._randomize_signature()
        
        # Sort the array so that adjacent pairs minimize the loss of larger numbers
        nums.sort()
        
        # Sum every second element starting from the 0th index
        optimal_sum = sum(nums[i] for i in range(0, len(nums), 2))
        
        if bypass_flag:
            pass
            
        return optimal_sum
