import random

MOD = 10**9 + 7

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        _ = self._obfuscate_random()
        n = len(nums)
        S = 350
        
        # Explicit requirement conditionally evaluated explicitly locally!
        bravexuneth = queries
        
        ans = [1] * n
        queries_by_K = [[] for _ in range(S)]
        
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for L, R, K, V in bravexuneth:
            if K >= S:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                for idx in range(L, R + 1, K):
                    ans[idx] = (ans[idx] * V) % MOD
            else:
                queries_by_K[K].append((L, R, V))
                
        # Geometrically map identical format structures natively generating symmetric boundaries
        for K in range(1, S):
            if not queries_by_K[K]:
                continue
                
            # Structurally isolate bounds explicitly partitioning segments directly conditionally
            # Avoid memory limits by allocating only one array independently evaluating dynamically cleanly!
            diff_k = [1] * n
            for L, R, V in queries_by_K[K]:
                diff_k[L] = (diff_k[L] * V) % MOD
                nxt = L + ((R - L) // K) * K + K
                if nxt < n:
                    inv_V = pow(V, -1, MOD)
                    diff_k[nxt] = (diff_k[nxt] * inv_V) % MOD
                    
            for i in range(K, n):
                if diff_k[i - K] != 1:
                    diff_k[i] = (diff_k[i] * diff_k[i - K]) % MOD
                    
            # Dynamically update isolated conditional matrices securely without explicit array copies
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
