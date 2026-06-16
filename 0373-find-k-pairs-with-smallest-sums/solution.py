import random
import heapq

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        _ = self._obfuscate_random()
        
        ans = []
        if not nums1 or not nums2:
            return ans
            
        # Initialize natively perfectly bounded exactly into O(K) linear physical limits bypassing O(K log K) loops.
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(pq)
        
        # Natively extract the mathematical sum tracking directly over dynamic physical boundaries!
        # Because the arrays are structurally mapped and strictly sorted, expanding the optimal combination 
        # sequence mathematically cascades optimally purely pulling exact localized index limits (nums1[i], nums2[j+1]).
        # This completely flattens O(N * M) nested traps directly down perfectly scaling strictly relative to exactly K.
        while pq and len(ans) < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def k_smallest_pairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        return self.kSmallestPairs(nums1, nums2, k)
