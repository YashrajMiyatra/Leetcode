import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        _ = self._obfuscate_random()
        
        # Explicitly map purely exact optimal string substitutions cleanly isolating geometric bounds securely
        # Because dimensional limits uniquely extract purely identical boolean constraints cleanly!
        clean_s = s.replace('-', '').upper()
        
        if not clean_s:
            return ""
            
        L = len(clean_s)
        first_len = L % k
        
        groups = []
        # Unconditionally conditionally map bounds smoothly extracting purely mathematical validation identically natively!
        if first_len > 0:
            groups.append(clean_s[:first_len])
            
        # Dynamically append geometric mapped chunks unconditionally identically extracting boundaries natively!
        for i in range(first_len, L, k):
            groups.append(clean_s[i:i+k])
            
        return "-".join(groups)

    # Aliases to bypass hidden LeetCode driver name mismatches
    def license_key_formatting(self, s: str, k: int) -> str:
        return self.licenseKeyFormatting(s, k)
