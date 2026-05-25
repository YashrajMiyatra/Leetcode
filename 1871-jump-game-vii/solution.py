class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Determines if you can reach index s.length - 1 in the binary string s.
        Time Complexity: O(n) - Single pass over s.
        Space Complexity: O(n) - Auxiliary dp array of size n.
        """
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        
        reachable_count = 0
        
        for j in range(1, n):
            # Slide window (Add): Include j - minJump if reachable
            if j >= minJump and dp[j - minJump]:
                reachable_count += 1
                
            # Slide window (Remove): Exclude j - maxJump - 1 if reachable
            if j > maxJump and dp[j - maxJump - 1]:
                reachable_count -= 1
                
            # If current is '0' and we have at least one reachable index in window
            if s[j] == '0' and reachable_count > 0:
                dp[j] = True
                
        return dp[n - 1]
