class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        Time Complexity: O(n) - Single pass over the string s.
        Space Complexity: O(min(m, n)) - Hash map size is bounded by size of string n and alphabet size m.
        """
        # Map to store character last seen index: {char: index}
        char_map = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If the character is already in the window, shrink the window from the left
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Record the current character's index
            char_map[char] = right
            
            # Update the maximum length found
            max_len = max(max_len, right - left + 1)
            
        return max_len
