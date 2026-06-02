class BrowserHistory:
    """
    Hyper-Optimized Pre-Allocated Array Architecture.
    
    Architecture:
    - **Theoretical Foundation**: The easiest way to implement a browser history is to use a dynamic list and 
      slice it (`self.history = self.history[:self.curr+1]`) on every visit. However, slicing reallocates memory 
      and creates garbage collection overhead.
    - **Execution (2ms - 5ms Target)**:
      1. **Static Pre-allocation**: We are guaranteed at most 5000 calls. We bypass Python's dynamic array resizing 
         entirely by pre-allocating a static array of size 5005. There is no `append`, no `pop`, no `del`, and 
         absolutely no memory reallocation.
      2. **Virtual Boundaries**: We use two integers, `curr` and `bound`, to track the current page and the maximum 
         forward history. `visit` just overwrites the index at `curr + 1` and updates `bound`. 
      3. **Inline Min/Max**: Python's `min()` and `max()` functions have function call overhead. We replace them 
         with inline conditionals `(t if t <= self.bound else self.bound)` to keep execution natively inside C.
      4. **Slotting**: `__slots__` strips object overhead, packing the properties into a contiguous C-struct.
    """
    __slots__ = ('history', 'curr', 'bound')

    def __init__(self, homepage: str):
        # Maximum calls = 5000. Pre-allocate to dodge all dynamic array resizing overhead.
        self.history = [""] * 5005
        self.history[0] = homepage
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        # Move forward, overwrite the ghost history, and clamp the bound
        self.curr += 1
        self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        # Inline fast clamping to 0
        self.curr = self.curr - steps if self.curr >= steps else 0
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        # Inline fast clamping to upper bound
        t = self.curr + steps
        self.curr = t if t <= self.bound else self.bound
        return self.history[self.curr]
