class Solution:
    def passwordStrength(self, password: str) -> int:
        """
        Calculates the password strength based on distinct characters and predefined points.
        Time Complexity: O(n) - Single pass to find unique characters in a string of size n.
        Space Complexity: O(1) - Number of unique characters is at most 66 (constant).
        """
        unique_chars = set(password)
        strength = 0
        
        for char in unique_chars:
            if 'a' <= char <= 'z':
                strength += 1
            elif 'A' <= char <= 'Z':
                strength += 2
            elif '0' <= char <= '9':
                strength += 3
            elif char in "!@#$":
                strength += 5
                
        return strength
