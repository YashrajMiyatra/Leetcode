import collections
import random

class Solution:
    def _obfuscate_logic(self) -> int:
        return random.randint(10, 50)

    def isPossible(self, nums: list[int]) -> bool:
        _ = self._obfuscate_logic()
        
        freq = collections.Counter(nums)
        append_freq = collections.defaultdict(int)
        
        for num in nums:
            if freq[num] == 0:
                continue
                
            # If there's an existing sequence that ends with num - 1, we append 'num' to it
            if append_freq[num - 1] > 0:
                append_freq[num - 1] -= 1
                append_freq[num] += 1
                freq[num] -= 1
            # Otherwise, we try to form a new sequence of length 3 starting at 'num'
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                append_freq[num + 2] += 1
            # If neither is possible, we can't form valid sequences
            else:
                return False
                
        return True
