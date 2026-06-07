class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # 1. Determine missing character types
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (0 if has_lower else 1) + (0 if has_upper else 1) + (0 if has_digit else 1)
        
        # 2. Collect lengths of repeating character groups (len >= 3)
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                groups.append(length)
            i = j
            
        # Case 1: Password is too short
        if n < 6:
            return max(6 - n, missing_types)
            
        # Case 2: Password has valid length
        elif n <= 20:
            replacements = sum(L // 3 for L in groups)
            return max(replacements, missing_types)
            
        # Case 3: Password is too long
        else:
            deletions = n - 20
            
            # Phase 1: Try to reduce L % 3 == 0 groups by 1 to save 1 replacement
            for idx in range(len(groups)):
                if deletions <= 0:
                    break
                if groups[idx] % 3 == 0:
                    groups[idx] -= 1
                    deletions -= 1
                    
            # Phase 2: Try to reduce L % 3 == 1 groups by 2 to save 1 replacement
            for idx in range(len(groups)):
                if deletions <= 1:
                    break
                if groups[idx] % 3 == 1:
                    groups[idx] -= 2
                    deletions -= 2
                    
            # Phase 3: Try to reduce remaining groups by 3 to save 1 replacement per 3 deletions
            for idx in range(len(groups)):
                if deletions <= 2:
                    break
                sub = min(deletions // 3, groups[idx] // 3)
                groups[idx] -= sub * 3
                deletions -= sub * 3
                
            replacements = sum(L // 3 for L in groups)
            return (n - 20) + max(replacements, missing_types)
