class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        Calculates the prefix common array C of two integer permutations A and B.
        
        Time Complexity: O(n) - Single pass over the arrays with O(1) frequency lookups.
        Space Complexity: O(n) - Tracker list/dictionary of size n + 1.
        """
        n = len(A)
        seen = [0] * (n + 1)
        common_count = 0
        C = []
        
        for i in range(n):
            # Increment frequency for element in A
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                common_count += 1
                
            # Increment frequency for element in B
            seen[B[i]] += 1
            if seen[B[i]] == 2:
                common_count += 1
                
            C.append(common_count)
            
        return C
