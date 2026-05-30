class Node:
    """
    A strictly optimized Doubly Linked List node.
    Using __slots__ is mandatory to keep memory to an absolute minimum 
    since we could be allocating and deallocating nodes frequently.
    """
    __slots__ = ['count', 'keys', 'prev', 'next']
    def __init__(self, count: int = 0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    """
    Ultra-optimized All O(1) Data Structure.
    
    Architecture:
    - Doubly Linked List sorted by count.
    - Each Node contains a set of strings that share the exact same count.
    - Dictionary maps key -> specific Node to jump instantly in O(1).
    - Dummy head and tail nodes to massively reduce edge-case checking overhead.
    """
    __slots__ = ['head', 'tail', 'map']

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        node = self.map.get(key)
        
        if node:
            nxt = node.next
            new_count = node.count + 1
            
            # If the next node matches our new count, jump into it
            if nxt.count == new_count:
                nxt.keys.add(key)
                self.map[key] = nxt
            else:
                # Otherwise, dynamically create a new bucket inline
                new_node = Node(new_count)
                new_node.keys.add(key)
                self.map[key] = new_node
                
                new_node.prev = node
                new_node.next = nxt
                node.next = new_node
                nxt.prev = new_node
                
            # Remove key from the old bucket
            node.keys.remove(key)
            if not node.keys:
                # Garbage collect empty buckets instantly
                p = node.prev
                n = node.next
                p.next = n
                n.prev = p
        else:
            nxt = self.head.next
            if nxt.count == 1:
                nxt.keys.add(key)
                self.map[key] = nxt
            else:
                new_node = Node(1)
                new_node.keys.add(key)
                self.map[key] = new_node
                
                new_node.prev = self.head
                new_node.next = nxt
                self.head.next = new_node
                nxt.prev = new_node

    def dec(self, key: str) -> None:
        node = self.map[key]
        
        if node.count == 1:
            del self.map[key]
        else:
            prv = node.prev
            new_count = node.count - 1
            
            if prv.count == new_count:
                prv.keys.add(key)
                self.map[key] = prv
            else:
                new_node = Node(new_count)
                new_node.keys.add(key)
                self.map[key] = new_node
                
                new_node.prev = prv
                new_node.next = node
                prv.next = new_node
                node.prev = new_node
                
        node.keys.remove(key)
        if not node.keys:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p

    def getMaxKey(self) -> str:
        last = self.tail.prev
        # next(iter(set)) is the absolute fastest way to pull an arbitrary item in C
        return next(iter(last.keys)) if last is not self.head else ""

    def getMinKey(self) -> str:
        first = self.head.next
        return next(iter(first.keys)) if first is not self.tail else ""
