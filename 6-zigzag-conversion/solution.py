class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts the string s to a zigzag pattern on numRows.
        
        This mathematical jump approach is heavily optimized for BOTH memory and speed.
        Instead of allocating arrays of strings for each row, it directly calculates the 
        final index positions to construct the string in exactly one pass.
        
        Time Complexity: O(n)
        Space Complexity: O(n) strictly to construct the return string (optimal).
        """
        # Edge cases where the string doesn't zigzag
        if numRows == 1 or numRows >= len(s):
            return s
            
        n = len(s)
        cycle = 2 * numRows - 2
        res = []
        
        for i in range(numRows):
            for j in range(i, n, cycle):
                # The vertical character in the zigzag
                res.append(s[j])
                
                # The diagonal character in the zigzag (for inner rows)
                k = j + cycle - 2 * i
                if i != 0 and i != numRows - 1 and k < n:
                    res.append(s[k])
                    
        return ''.join(res)
