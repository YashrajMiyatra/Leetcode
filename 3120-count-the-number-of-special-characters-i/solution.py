class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Counts the number of special letters. A letter is special if it appears 
        both in lowercase and uppercase.
        
        Time Complexity: O(n) - where n is the length of the string, to build the set.
        Space Complexity: O(1) - the set contains at most 52 unique characters.
        """
        char_set = set(word)
        count = 0
        
        for i in range(26):
            if chr(97 + i) in char_set and chr(65 + i) in char_set:
                count += 1
                
        return count
