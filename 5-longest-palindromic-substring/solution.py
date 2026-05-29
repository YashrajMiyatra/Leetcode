class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring using the Expand Around Center approach.
        
        Time Complexity: O(n^2) where n is the length of the string.
        Space Complexity: O(1) as we only store the indices of the longest palindrome.
        """
        if not s:
            return ""
            
        start, max_len = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
            
        for i in range(len(s)):
            # Odd length palindromes centered at i
            len1 = expand_around_center(i, i)
            # Even length palindromes centered between i and i+1
            len2 = expand_around_center(i, i + 1)
            
            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                # If length is odd, i is center. start = i - len//2
                # If length is even, i is left center. start = i - (len-1)//2
                start = i - (curr_max - 1) // 2
                
        return s[start:start + max_len]
