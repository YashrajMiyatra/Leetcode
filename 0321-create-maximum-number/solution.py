from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        
        # Helper to get the lexicographically largest subsequence of length x
        def maxSubsequence(nums: List[int], x: int) -> List[int]:
            stack = []
            drop = len(nums) - x
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:x]
            
        # Helper to merge two lists to form the largest possible number
        def merge(A: List[int], B: List[int]) -> List[int]:
            res = []
            p1, p2 = 0, 0
            while p1 < len(A) and p2 < len(B):
                # Compare remaining suffixes lexicographically
                if A[p1:] > B[p2:]:
                    res.append(A[p1])
                    p1 += 1
                else:
                    res.append(B[p2])
                    p2 += 1
            res.extend(A[p1:])
            res.extend(B[p2:])
            return res
            
        best = []
        # Try all valid splits between nums1 and nums2
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = maxSubsequence(nums1, i)
            sub2 = maxSubsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > best:
                best = candidate
                
        return best
