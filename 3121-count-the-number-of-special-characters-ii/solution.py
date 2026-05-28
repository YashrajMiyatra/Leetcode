class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Counts the number of special letters. A letter is special if it appears both in
        lowercase and uppercase, and every lowercase occurrence appears before the first
        uppercase occurrence.
        
        Time Complexity: O(n) - Single pass through the string.
        Space Complexity: O(1) - Fixed size arrays of length 26.
        """
        last_lower = [-1] * 26
        first_upper = [-1] * 26
        
        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                last_lower[ord(char) - 97] = i
            else:
                idx = ord(char) - 65
                if first_upper[idx] == -1:
                    first_upper[idx] = i
                    
        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1 and last_lower[i] < first_upper[i]:
                count += 1
                
        return count
