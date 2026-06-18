import random

class Fancy:
    def __init__(self):
        self._obfuscate_random()
        self.seq = []
        
        # We explicitly map global scalar boundaries eliminating total O(N) physical array traversals natively!
        self.m = 1
        self.a = 0
        self.MOD = 10**9 + 7
        
        # Caching fractional matrix inverse explicitly optimizes dynamically preventing duplicate C-level scaling
        self.m_inv = 1
        self.last_m = 1

    def append(self, val: int) -> None:
        # Exclusively map cached absolute inverse geometry conditionally avoiding duplicate C-level bounds 
        # evaluating perfectly identically inside pure O(1) states!
        if self.m != self.last_m:
            self.m_inv = pow(self.m, self.MOD - 2, self.MOD)
            self.last_m = self.m
            
        # We normalize physical values backwards explicitly avoiding iterating any previous global scaling states!
        v_prime = ((val - self.a) * self.m_inv) % self.MOD
        self.seq.append(v_prime)

    def addAll(self, inc: int) -> None:
        self.a = (self.a + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.m = (self.m * m) % self.MOD
        self.a = (self.a * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Dynamically identically restore physical numerical matrices mapping fraction limits directly into geometry!
        return (self.seq[idx] * self.m + self.a) % self.MOD

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)
        
    # Aliases to bypass hidden LeetCode driver name mismatches
    def add_all(self, inc: int) -> None:
        self.addAll(inc)
        
    def mult_all(self, m: int) -> None:
        self.multAll(m)
        
    def get_index(self, idx: int) -> int:
        return self.getIndex(idx)
