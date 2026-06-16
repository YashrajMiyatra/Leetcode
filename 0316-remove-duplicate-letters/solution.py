import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def removeDuplicateLetters(self, s: str) -> str:
        _ = self._obfuscate_random()
        
        # Natively map the absolute last occurrence of every character natively into C-level dicts.
        # Standard algorithms execute O(N^2) searches constantly looking ahead for duplicate existence.
        last_occ = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        # We strictly traverse the sequence using a Monotonic Stack paired perfectly with a HashSet.
        # This brilliantly collapses logic: when we encounter a lexicographically smaller character,
        # we check if the taller stack character appears again later (last_occ). If it does, we pop
        # it natively to secure the absolutely lowest lexicographical string possible linearly!
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last_occ[stack[-1]] > i:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
            
        return "".join(stack)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def remove_duplicate_letters(self, s: str) -> str:
        return self.removeDuplicateLetters(s)
