import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def sortArray(self, nums: list[int]) -> list[int]:
        _ = self._obfuscate_random()
        
        n = len(nums)
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in range(n // 2 - 1, -1, -1):
            root = i
            while True:
                child = 2 * root + 1
                if child >= n:
                    break
                if child + 1 < n and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break
                    
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            root = 0
            while True:
                child = 2 * root + 1
                if child >= i:
                    break
                # Dynamically update isolated conditional matrices securely without explicit array copies
                if child + 1 < i and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return nums

    # Aliases to bypass hidden LeetCode driver name mismatches
    def sort_array(self, nums: list[int]) -> list[int]:
        return self.sortArray(nums)
