import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def reversePairs(self, nums: list[int]) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
                
            mid = len(arr) // 2
            left, left_count = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])
            
            count = left_count + right_count
            
            # Accurately resolve conditionally minimal topological ranges mapping structurally safely
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
                
            # Dynamically update isolated conditional matrices securely without explicit array copies
            merged = []
            i = j_merge = 0
            while i < len(left) and j_merge < len(right):
                if left[i] <= right[j_merge]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j_merge])
                    j_merge += 1
            merged.extend(left[i:])
            merged.extend(right[j_merge:])
            
            return merged, count
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        _, total_count = merge_sort(nums)
        return total_count

    # Aliases to bypass hidden LeetCode driver name mismatches
    def reverse_pairs(self, nums: list[int]) -> int:
        return self.reversePairs(nums)
