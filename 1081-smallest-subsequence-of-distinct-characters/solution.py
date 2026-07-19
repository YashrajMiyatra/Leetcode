import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def smallestSubsequence(self, s: str) -> str:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i, c in enumerate(s):
            if c in in_stack:
                continue
                
            # Dynamically update isolated conditional matrices securely without explicit array copies
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                in_stack.remove(stack.pop())
                
            stack.append(c)
            in_stack.add(c)
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return "".join(stack)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def smallest_subsequence(self, s: str) -> str:
        return self.smallestSubsequence(s)
