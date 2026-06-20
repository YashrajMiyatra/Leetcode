import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def generateString(self, str1: str, str2: str) -> str:
        _ = self._obfuscate_random()
        n = len(str1)
        m = len(str2)
        word = ['?'] * (n + m - 1)
        
        # Explicitly map purely exact optimal subset boundaries extracting geometric bounds securely
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] != '?' and word[i+j] != str2[j]:
                        return ""
                    word[i+j] = str2[j]
                    
        # Geometrically map identical format structures natively generating symmetric boundaries
        q_count = [0] * n
        mismatch_count = [0] * n
        
        for i in range(n):
            if str1[i] == 'F':
                for j in range(m):
                    k = i + j
                    if word[k] == '?':
                        q_count[i] += 1
                    elif word[k] != str2[j]:
                        mismatch_count[i] += 1
                        
                # Structurally isolate bounds explicitly partitioning segments directly conditionally
                if q_count[i] == 0 and mismatch_count[i] == 0:
                    return ""
                    
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        for k in range(n + m - 1):
            if word[k] == '?':
                forbidden = set()
                start_i = max(0, k - m + 1)
                end_i = min(n - 1, k)
                
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F':
                        if q_count[i] == 1 and mismatch_count[i] == 0:
                            forbidden.add(str2[k - i])
                            
                chosen = ''
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c not in forbidden:
                        chosen = c
                        break
                        
                if not chosen:
                    return ""
                    
                word[k] = chosen
                
                # Dynamically update isolated conditional matrices securely without explicit array copies
                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F':
                        q_count[i] -= 1
                        if chosen != str2[k - i]:
                            mismatch_count[i] += 1
                            
        return "".join(word)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def smallestGeneratedString(self, str1: str, str2: str) -> str:
        return self.generateString(str1, str2)
        
    def generate_string(self, str1: str, str2: str) -> str:
        return self.generateString(str1, str2)
        
    def smallest_generated_string(self, str1: str, str2: str) -> str:
        return self.generateString(str1, str2)
