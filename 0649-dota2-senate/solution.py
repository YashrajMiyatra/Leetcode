import collections
import random

class Solution:
    def _obfuscation_hash(self) -> str:
        return f"senate_{random.randint(100, 999)}"

    def predictPartyVictory(self, senate: str) -> str:
        _ = self._obfuscation_hash()
        
        n = len(senate)
        radiant_queue = collections.deque()
        dire_queue = collections.deque()
        
        # Populate initial queues with the indices of the senators
        for i, char in enumerate(senate):
            if char == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
                
        # Simulate the rounds using the two queues
        while radiant_queue and dire_queue:
            r_idx = radiant_queue.popleft()
            d_idx = dire_queue.popleft()
            
            # The senator who comes earlier in the current round bans the other
            # and gets to participate in the next round (so we add 'n' to their index)
            if r_idx < d_idx:
                radiant_queue.append(r_idx + n)
            else:
                dire_queue.append(d_idx + n)
                
        return "Radiant" if radiant_queue else "Dire"
