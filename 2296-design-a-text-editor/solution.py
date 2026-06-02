class TextEditor:
    """
    Hyper-Optimized O(k) Dual-Stack Architecture for Text Editor.
    
    Architecture:
    - **Theoretical Foundation**: A standard text editor's cursor acts exactly like the partition between two 
      stacks (left and right). Instead of maintaining a single monolithic string or array and shifting memory O(N) 
      on every insert/delete, a Dual-Stack pushes and pops purely at the boundary where the cursor lives. 
      This mathematically guarantees O(k) per operation instead of O(N).
    - **Execution (2ms - 5ms Target)**:
      1. **Native String Iteration**: `self.left.extend(text)` natively loops through the string in C without 
         requiring a manual Python `list(text)` conversion.
      2. **O(k) Slicing & Memmove**: Deleting and shifting k elements is done via `del self.left[-k:]` and 
         `self.left[-k:]`. Python translates these directly into C-level `memmove` operations, dodging Python 
         bytecode loops entirely.
      3. **Zero-Overhead Reversals**: `reversed()` creates a lightweight C-iterator that consumes no extra memory 
         array, feeding directly into `.extend()`.
      4. **Slotting**: `__slots__` strips out the dynamic `__dict__` overhead, locking the memory structure and 
         accelerating property lookups.
    """
    __slots__ = ('left', 'right')

    def __init__(self):
        # Left stack represents text before the cursor.
        self.left = []
        # Right stack represents text after the cursor (stored in reverse for O(1) popping).
        self.right = []

    def addText(self, text: str) -> None:
        # Natively iterates and extends in C
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        # Inline min() to bypass function call overhead
        k = k if k <= len(self.left) else len(self.left)
        if k:
            # Natively triggers a C-level memmove array shrink
            del self.left[-k:]
        return k

    def cursorLeft(self, k: int) -> str:
        k = k if k <= len(self.left) else len(self.left)
        if k:
            # Extract the chunk, reverse it using a zero-overhead iterator, and inject it to the right stack
            self.right.extend(reversed(self.left[-k:]))
            del self.left[-k:]
            
        # Fast list-to-string concatenation of the last 10 characters
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        k = k if k <= len(self.right) else len(self.right)
        if k:
            # Extract from right stack, reverse it, and inject to the left stack
            self.left.extend(reversed(self.right[-k:]))
            del self.right[-k:]
            
        return "".join(self.left[-10:])
