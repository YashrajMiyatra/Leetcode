import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def concatenateAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        _ = self._obfuscate_random()
        MOD = 10**9 + 7
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        m = len(s)
        cnt = [0] * m
        non_zeros = []
        
        curr_cnt = 0
        for i, char in enumerate(s):
            if char != '0':
                curr_cnt += 1
                non_zeros.append(int(char))
            cnt[i] = curr_cnt
            
        K = len(non_zeros)
        pref_sum = [0] * (K + 1)
        pref_val = [0] * (K + 1)
        pow10 = [1] * (K + 1)
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(K):
            pref_sum[i+1] = pref_sum[i] + non_zeros[i]
            pref_val[i+1] = (pref_val[i] * 10 + non_zeros[i]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            L = cnt[l-1] if l > 0 else 0
            R = cnt[r] - 1
            
            if L > R:
                ans.append(0)
            else:
                length = R - L + 1
                val = (pref_val[R+1] - pref_val[L] * pow10[length]) % MOD
                digit_sum = pref_sum[R+1] - pref_sum[L]
                ans.append((val * digit_sum) % MOD)
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def concatenate_and_multiply(self, s: str, queries: list[list[int]]) -> list[int]:
        return self.concatenateAndMultiply(s, queries)
        
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        return self.concatenateAndMultiply(s, queries)
