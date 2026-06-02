class Node:
    # Hyper-optimization 1: __slots__ blocks dynamic __dict__ creation, stripping memory overhead and 
    # massively accelerating property lookups directly at the C-level.
    __slots__ = ('count', 'keys', 'prev', 'next')
    
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    """
    Hyper-Optimized Constant Time (O(1)) Frequency Tracker.
    
    Architecture:
    - **Theoretical Foundation**: Achieving O(1) across increment, decrement, getMax, and getMin requires 
      a perfectly synchronized Doubly Linked List (DLL) mapping to Hash Sets. The DLL maintains the relative 
      order of frequencies, while the Hash Map guarantees O(1) lookups for any key's current bucket.
    - **Execution (2ms - 5ms Target)**:
      1. **Slotting**: Nodes are constrained via `__slots__` to ensure the tightest possible memory packing.
      2. **Inlining**: Helper functions (`_insert`, `_remove`) are entirely stripped and manually inlined. 
         Function call overhead in Python can easily push an O(1) algorithm beyond the 5ms boundary if it's 
         called 50,000 times. We manually inline all pointer operations.
      3. **Identity vs Equality**: We use `is` instead of `==` for Sentinel checks (e.g., `nxt is self.tail`). 
         This skips Python's `__eq__` dunder resolution and directly compares memory addresses natively.
      4. **Native Iterators**: Max and Min retrievals use `next(iter(keys))`. This evaluates entirely in C 
         and fetches an arbitrary set element in O(1) without casting the set to a list or looping.
    """
    __slots__ = ('head', 'tail', 'map')
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.count
            node.keys.remove(key)
            
            nxt = node.next
            if nxt is self.tail or nxt.count != freq + 1:
                new_node = Node(freq + 1)
                # Inline insertion: After 'node'
                new_node.prev = node
                new_node.next = nxt
                node.next = new_node
                nxt.prev = new_node
                nxt = new_node
                
            nxt.keys.add(key)
            self.map[key] = nxt
            
            if not node.keys:
                # Inline removal: Delete 'node'
                p = node.prev
                n = node.next
                p.next = n
                n.prev = p
        else:
            nxt = self.head.next
            if nxt is self.tail or nxt.count != 1:
                new_node = Node(1)
                # Inline insertion: After 'head'
                new_node.prev = self.head
                new_node.next = nxt
                self.head.next = new_node
                nxt.prev = new_node
                nxt = new_node
            
            nxt.keys.add(key)
            self.map[key] = nxt

    def dec(self, key: str) -> None:
        node = self.map[key]
        freq = node.count
        node.keys.remove(key)
        
        if freq == 1:
            del self.map[key]
        else:
            prv = node.prev
            if prv is self.head or prv.count != freq - 1:
                new_node = Node(freq - 1)
                # Inline insertion: Before 'node'
                new_node.next = node
                new_node.prev = prv
                prv.next = new_node
                node.prev = new_node
                prv = new_node
                
            prv.keys.add(key)
            self.map[key] = prv
            
        if not node.keys:
            # Inline removal: Delete 'node'
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p

    def getMaxKey(self) -> str:
        # C-level iterator fetch; bypasses Python loops entirely
        return next(iter(self.tail.prev.keys)) if self.tail.prev is not self.head else ""

    def getMinKey(self) -> str:
        # C-level iterator fetch
        return next(iter(self.head.next.keys)) if self.head.next is not self.tail else ""
