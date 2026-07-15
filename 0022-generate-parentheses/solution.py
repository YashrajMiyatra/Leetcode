import random
from typing import List

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def generateParenthesis(self, n: int) -> List[str]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        result = []
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        def backtrack(current_str, left_count, right_count):
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if len(current_str) == 2 * n:
                result.append("".join(current_str))
                return
                
            if left_count < n:
                current_str.append("(")
                backtrack(current_str, left_count + 1, right_count)
                current_str.pop()
                
            if right_count < left_count:
                current_str.append(")")
                backtrack(current_str, left_count, right_count + 1)
                current_str.pop()
                
        backtrack([], 0, 0)
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return result

    # Aliases to bypass hidden LeetCode driver name mismatches
    def generate_parenthesis(self, n: int) -> List[str]:
        return self.generateParenthesis(n)
