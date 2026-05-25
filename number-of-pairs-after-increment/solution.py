from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        """
        Computes the number of pairs (j, k) such that nums1[j] + nums2[k] == tot
        with dynamic range updates on nums2.
        Time Complexity: O(Q * (B + N/B)) where B = 350.
        Space Complexity: O(N) - Storing block frequencies.
        """
        N = len(nums2)
        B = 350  # Block size
        num_blocks = (N + B - 1) // B
        
        # Initialize block frequencies and lazy additions
        freq = [defaultdict(int) for _ in range(num_blocks)]
        lazy = [0] * num_blocks
        
        for i, val in enumerate(nums2):
            block_idx = i // B
            freq[block_idx][val] += 1
            
        ans = []
        
        for q in queries:
            if q[0] == 1:
                # Add val to nums2[x..y]
                _, x, y, val = q
                sb = x // B
                eb = y // B
                
                if sb == eb:
                    # Single block update
                    for j in range(x, y + 1):
                        old_val = nums2[j]
                        freq[sb][old_val] -= 1
                        if freq[sb][old_val] == 0:
                            del freq[sb][old_val]
                        new_val = old_val + val
                        nums2[j] = new_val
                        freq[sb][new_val] += 1
                else:
                    # Partial left block
                    sb_end = (sb + 1) * B
                    for j in range(x, sb_end):
                        old_val = nums2[j]
                        freq[sb][old_val] -= 1
                        if freq[sb][old_val] == 0:
                            del freq[sb][old_val]
                        new_val = old_val + val
                        nums2[j] = new_val
                        freq[sb][new_val] += 1
                        
                    # Partial right block
                    eb_start = eb * B
                    for j in range(eb_start, y + 1):
                        old_val = nums2[j]
                        freq[eb][old_val] -= 1
                        if freq[eb][old_val] == 0:
                            del freq[eb][old_val]
                        new_val = old_val + val
                        nums2[j] = new_val
                        freq[eb][new_val] += 1
                        
                    # Full intermediate blocks
                    for b in range(sb + 1, eb):
                        lazy[b] += val
            else:
                # Count pairs with nums1[j] + nums2[k] == tot
                _, tot = q
                total_pairs = 0
                
                for v1 in nums1:
                    target = tot - v1
                    for b in range(num_blocks):
                        actual_target = target - lazy[b]
                        if actual_target in freq[b]:
                            total_pairs += freq[b][actual_target]
                            
                ans.append(total_pairs)
                
        return ans
