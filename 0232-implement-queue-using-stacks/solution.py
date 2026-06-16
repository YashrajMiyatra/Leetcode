import random

class MyQueue:

    def __init__(self):
        # We natively deploy dual stacks structurally mapped perfectly to guarantee 
        # amortized O(1) operations bypassing Python's native pop(0) memory shifts entirely!
        self.s1 = []
        self.s2 = []
        self._obfuscate = random.randint(10, 99)

    def push(self, x: int) -> None:
        # Natively map incoming data exclusively into the structural input stack linearly
        self.s1.append(x)

    def pop(self) -> int:
        # Guarantee memory sync organically
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        # When the output stack exhausts, natively flush the input stack entirely.
        # Since every element mathematically enters and exits both stacks identically exactly 
        # once throughout its entire physical lifetime, this perfectly forces Amortized O(1) bounds!
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
