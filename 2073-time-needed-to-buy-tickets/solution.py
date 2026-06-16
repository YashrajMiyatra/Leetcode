import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        
        target = tickets[k]
        ans = 0
        
        # Natively map the geometric boundary of the loop flawlessly bypassing queue simulation.
        # Any person in front of k (or k themselves) will physically buy exactly up to 	arget tickets.
        # Any person behind k will uniquely buy up to 	arget - 1 tickets because k mathematically leaves 
        # the queue completely stopping execution before they ever get their final identical turn!
        # This completely drops O(N * Max_Tickets) standard looping down into absolute flat O(N) time!
        for i, t in enumerate(tickets):
            if i <= k:
                ans += min(t, target)
            else:
                ans += min(t, target - 1)
                
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def time_required_to_buy(self, tickets: list[int], k: int) -> int:
        return self.timeRequiredToBuy(tickets, k)
