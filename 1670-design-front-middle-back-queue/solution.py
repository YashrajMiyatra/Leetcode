from collections import deque

class FrontMiddleBackQueue:
    """
    Hyper-Optimized Dual-Deque Architecture (O(1) strictly bound time complexity).
    
    Architecture:
    - **Theoretical Foundation**: Pushing and popping from the middle of a continuous array is intrinsically O(N) due to 
      memory shifting (memmove). To achieve mathematically pure O(1) operations across Front, Middle, and Back, we split 
      the queue precisely in half into two standard Double Ended Queues (`left` and `right`).
    - **Execution (2ms - 5ms Target)**:
      1. **C-Compiled Deques**: Python's `collections.deque` is a fully C-compiled doubly linked list of fixed-size blocks. 
         Pushing/popping at ends is strictly O(1) at the physical level.
      2. **Asymmetric Balancing**: We maintain the strict invariant `0 <= len(right) - len(left) <= 1`. The `right` queue 
         absorbs the odd element. This elegantly maps Python's default division rules (`// 2`) directly to the queues, 
         completely eliminating off-by-one errors.
      3. **Stripping Helper Methods**: Instead of writing a `_balance()` helper function, I manually inlined the minimal 
         required balancing checks natively inside each function. This saves tens of thousands of function call frame creations 
         over the course of execution.
      4. **Slotting**: `__slots__` strips object overhead, accelerating lookup times for `self.left` and `self.right`.
    """
    __slots__ = ('left', 'right')

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        # Re-balance if left exceeds right
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

    def pushMiddle(self, val: int) -> None:
        # Based on our invariant, if they are equal, the new element goes to right
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        # Re-balance if right exceeds left by 2
        if len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def popFront(self) -> int:
        if not self.right:
            return -1
        
        # Pop from left if it exists, otherwise from right (case where only 1 element exists)
        val = self.left.popleft() if self.left else self.right.popleft()
        
        # Re-balance if right exceeds left by 2
        if len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())
        return val

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        
        # Since right holds the extra odd element, equality means even total elements.
        # Problem specifies popping the left-leaning middle for even lengths.
        val = self.left.pop() if len(self.left) == len(self.right) else self.right.popleft()
        # No re-balance needed! If even, popping left means right is left + 1 (Valid). 
        # If odd, popping right means left == right (Valid).
        return val

    def popBack(self) -> int:
        if not self.right:
            return -1
            
        val = self.right.pop()
        
        # Re-balance if left now exceeds right
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        return val
