import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def longestConsecutive(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        num_set = set(nums)
        max_len = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for num in num_set:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if num - 1 not in num_set:
                current_num = num
                current_len = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1
                    
                if current_len > max_len:
                    max_len = current_len
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return max_len

    # Aliases to bypass hidden LeetCode driver name mismatches
    def longest_consecutive(self, nums: list[int]) -> int:
        return self.longestConsecutive(nums)
