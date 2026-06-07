import random

class Solution:
    def _random_identifier_generator(self) -> int:
        return random.randint(500, 999)

    def findLongestChain(self, pairs: list[list[int]]) -> int:
        _ = self._random_identifier_generator()
        
        # Sort pairs greedily by their right boundary
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        chain_length = 0
        
        for left, right in pairs:
            # If the start of the current pair is strictly greater than
            # the end of the previous pair in our chain, we can add it.
            if left > current_end:
                chain_length += 1
                current_end = right
                
        return chain_length
