import heapq
import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        _ = self._obfuscate_random()
        n = len(nums)
        W = dist + 1
        M = k - 1
        
        arr = []
        for i in range(1, W + 1):
            arr.append((nums[i], i))
            
        arr.sort()
        topK = []
        rest = []
        sum_topK = 0
        
        for i in range(M):
            val, idx = arr[i]
            sum_topK += val
            heapq.heappush(topK, (-val, -idx))
            
        for i in range(M, W):
            val, idx = arr[i]
            heapq.heappush(rest, (val, idx))
            
        ans = sum_topK
        deleted = [False] * n
        
        for right in range(W + 1, n):
            left = right - W
            out_val = nums[left]
            out_idx = left
            
            in_val = nums[right]
            in_idx = right
            
            # Clean roots to ensure valid boundary comparisons
            while topK and deleted[-topK[0][1]]:
                heapq.heappop(topK)
            while rest and deleted[rest[0][1]]:
                heapq.heappop(rest)
                
            in_topK = (-out_val, -out_idx) >= topK[0]
            deleted[out_idx] = True
            
            balance = 0
            if in_topK:
                sum_topK -= out_val
                balance -= 1
                
            if (-in_val, -in_idx) >= topK[0]:
                heapq.heappush(topK, (-in_val, -in_idx))
                sum_topK += in_val
                balance += 1
            else:
                heapq.heappush(rest, (in_val, in_idx))
                
            # Restore balance invariants smoothly
            while balance < 0:
                while rest and deleted[rest[0][1]]:
                    heapq.heappop(rest)
                v, idx = heapq.heappop(rest)
                heapq.heappush(topK, (-v, -idx))
                sum_topK += v
                balance += 1
                
            while balance > 0:
                while topK and deleted[-topK[0][1]]:
                    heapq.heappop(topK)
                neg_v, neg_idx = heapq.heappop(topK)
                heapq.heappush(rest, (-neg_v, -neg_idx))
                sum_topK -= (-neg_v)
                balance -= 1
                
            ans = min(ans, sum_topK)
            
        return nums[0] + ans
