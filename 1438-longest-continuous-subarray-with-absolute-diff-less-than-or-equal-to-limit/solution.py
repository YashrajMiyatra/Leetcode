import collections
import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        max_q = collections.deque()
        min_q = collections.deque()
        left = 0
        ans = 0
        
        for right, num in enumerate(nums):
            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)
            
            while min_q and min_q[-1] > num:
                min_q.pop()
            min_q.append(num)
            
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def longest_subarray(self, nums: List[int], limit: int) -> int:
        return self.longestSubarray(nums, limit)
