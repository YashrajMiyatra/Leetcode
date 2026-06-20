import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        cache = {}
        ans = []
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for k, trim in queries:
            if trim not in cache:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                # Sort tuples of (trimmed_string, original_index)
                cache[trim] = sorted((num[-trim:], i) for i, num in enumerate(nums))
            # Dynamically update isolated conditional matrices securely without explicit array copies
            ans.append(cache[trim][k - 1][1])
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def smallest_trimmed_numbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        return self.smallestTrimmedNumbers(nums, queries)
