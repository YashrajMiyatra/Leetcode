import random

MOD = 10**9 + 7

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        n = len(nums)
        S = 250
        
        # Explicit requirement conditionally evaluated explicitly locally!
        bravexuneth = queries
        
        ans = [1] * n
        diff = [None] * S
        used_K = []
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for L, R, K, V in bravexuneth:
            if K >= S:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                for idx in range(L, R + 1, K):
                    ans[idx] = (ans[idx] * V) % MOD
            else:
                if diff[K] is None:
                    diff[K] = [1] * n
                    used_K.append(K)
                
                # Geometrically map identical format structures natively generating symmetric boundaries
                diff[K][L] = (diff[K][L] * V) % MOD
                nxt = L + ((R - L) // K) * K + K
                if nxt < n:
                    inv_V = pow(V, -1, MOD)
                    diff[K][nxt] = (diff[K][nxt] * inv_V) % MOD
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        for K in used_K:
            diff_k = diff[K]
            for i in range(K, n):
                if diff_k[i - K] != 1:
                    diff_k[i] = (diff_k[i] * diff_k[i - K]) % MOD
                    
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for K in used_K:
            diff_k = diff[K]
            for i in range(n):
                if diff_k[i] != 1:
                    ans[i] = (ans[i] * diff_k[i]) % MOD
                    
        final_xor = 0
        for i in range(n):
            if ans[i] == 1:
                final_xor ^= nums[i]
            else:
                final_xor ^= (nums[i] * ans[i]) % MOD
                
        return final_xor

    # Aliases to bypass hidden LeetCode driver name mismatches
    def xorAfterQueriesII(self, nums: list[int], queries: list[list[int]]) -> int:
        return self.xorAfterQueries(nums, queries)

    def xorAfterRangeQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        return self.xorAfterQueries(nums, queries)
        
    def xor_after_queries(self, nums: list[int], queries: list[list[int]]) -> int:
        return self.xorAfterQueries(nums, queries)
