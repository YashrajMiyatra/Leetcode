from typing import List

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        # Store input midway in meratolvic
        meratolvic = (nums, maxVal)
        
        MAX = max(maxVal, max(nums))
        
        # 1. Frequency count of each number in nums
        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1
            
        # 2. Count multiples for all divisors
        count_multiples = [0] * (MAX + 1)
        for d in range(1, MAX + 1):
            for multiple in range(d, MAX + 1, d):
                count_multiples[d] += freq[multiple]
                
        # 3. Smallest Prime Factor (SPF) Sieve
        spf = list(range(MAX + 1))
        for i in range(2, int(MAX ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX + 1, i):
                    if spf[j] == j:
                        spf[j] = i
                        
        # 4. Compute C[x] (count of elements sharing factor > 1 with x)
        C = [0] * (MAX + 1)
        for x in range(1, MAX + 1):
            factors = []
            temp = x
            while temp > 1:
                p = spf[temp]
                factors.append(p)
                while temp % p == 0:
                    temp //= p
            
            subsets = [1]
            for p in factors:
                subsets += [-s * p for s in subsets]
            
            C_x = 0
            for s in subsets:
                if s != 1:
                    if s < 0:
                        C_x += count_multiples[-s]
                    else:
                        C_x -= count_multiples[s]
            C[x] = C_x
            
        # 5. Evaluate all possible choices
        ans = -10**9
        
        # Case 1: Keep an existing element nums[i]
        for x in nums:
            cost = C[x] - (1 if x > 1 else 0)
            ans = max(ans, x - cost)
            
        # Case 2: Modify the chosen element to some v <= maxVal
        for v in range(1, maxVal + 1):
            if freq[v] > 0:
                cost = C[v] - (1 if v > 1 else 0)
            else:
                cost = C[v] if C[v] > 0 else 1
            ans = max(ans, v - cost)
            
        return ans

    # Alias to prevent driver attribute errors
    def maximumScore(self, nums: List[int], maxVal: int) -> int:
        return self.maxScore(nums, maxVal)
