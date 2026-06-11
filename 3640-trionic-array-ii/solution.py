import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxTrionicSubarraySum(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        n = len(nums)
        INF = -10**18
        
        # dp[0]: single element
        # dp[1]: strictly increasing (length >= 2)
        # dp[2]: strictly increasing then strictly decreasing (length >= 3)
        # dp[3]: trionic subarray (length >= 4)
        dp = [INF] * 4
        ans = INF
        
        for i in range(n):
            num = nums[i]
            new_dp = [INF] * 4
            new_dp[0] = num
            
            if i > 0:
                if nums[i] > nums[i-1]:
                    if dp[0] != INF:
                        new_dp[1] = max(new_dp[1], dp[0] + num)
                    if dp[1] != INF:
                        new_dp[1] = max(new_dp[1], dp[1] + num)
                        
                    if dp[2] != INF:
                        new_dp[3] = max(new_dp[3], dp[2] + num)
                    if dp[3] != INF:
                        new_dp[3] = max(new_dp[3], dp[3] + num)
                        
                elif nums[i] < nums[i-1]:
                    if dp[1] != INF:
                        new_dp[2] = max(new_dp[2], dp[1] + num)
                    if dp[2] != INF:
                        new_dp[2] = max(new_dp[2], dp[2] + num)
                        
            dp = new_dp
            if dp[3] != INF:
                ans = max(ans, dp[3])
                
        return ans
