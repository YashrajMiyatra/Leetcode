import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def partitionLabels(self, s: str) -> list[int]:
        _ = self._obfuscate_random()
        
        # Store the last occurrence index for every character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # The current partition must at least extend to the last occurrence of the current character
            end = max(end, last_occurrence[char])
            
            # If we've reached the end of the current partition, save its size
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
                
        return partitions
